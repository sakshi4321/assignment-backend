from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Item
from postgresdb.serializers import ItemSerializer
from rest_framework import viewsets
from .models import Category
from .serializers import CategorySerializer
from .serializers import UserRegistrationSerializer
from rest_framework import status, views
from django.contrib.auth import authenticate

from .serializers import UserLoginSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def get_queryset(self):
        queryset = Item.objects.all()
        category_id = self.request.query_params.get('category', None)

        # If category_id is provided, filter by that category
        if category_id:
            queryset = queryset.filter(category__id=category_id)

        return queryset


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class UserRegistrationView(views.APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            # Assuming you have some mechanism to create or return a token
            return Response({"message": "Login successful"}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)