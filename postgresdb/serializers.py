from rest_framework import serializers
from .models import Item, Category
from .models import UserCredentials
from django.contrib.auth.hashers import check_password

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'category']

class ItemSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())

    class Meta:
        model = Item
        fields = ['sku', 'name', 'category', 'tags', 'inStock', 'availableStock']

    def get_category_details(self, obj):
        """
        This method fetches more detailed information about the category
        associated with the item.
        """
        category = Category.objects.get(id=obj.category.id)
        return CategorySerializer(category).data

    def to_representation(self, instance):
        """
        Customize the JSON representation of the Item.
        """
        representation = super().to_representation(instance)
        # Adds detailed category info directly into the representation
        category_representation = self.get_category_details(instance)
        representation['category_details'] = category_representation
        return representation
    

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCredentials
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserCredentials.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user
class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)

    def validate(self, data):
        # Try to retrieve the user by username
        try:
            user = UserCredentials.objects.get(username=data['username'])
        except UserCredentials.DoesNotExist:
            raise serializers.ValidationError("Invalid username or password")

        # Check the password
        if not check_password(data['password'], user.password):
            raise serializers.ValidationError("Invalid username or password")

        # Return the user object if validation is successful
        return user