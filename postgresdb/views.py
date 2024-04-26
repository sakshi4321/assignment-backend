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
        """"Returns the queryset of all items or filtered by category_id if provided."
        Parameters:
            - self (object): The current instance of the class.
            - category_id (int): The ID of the category to filter by, if provided.
        Returns:
            - queryset (object): The queryset of all items or filtered by category_id if provided.
        Processing Logic:
            - Get all items from the Item model.
            - Get the category_id from the request query parameters.
            - If category_id is provided, filter the queryset by that category.
            - Return the filtered or unfiltered queryset."""
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
        """This function handles user login and returns a response based on the validity of the serializer.
        Parameters:
            - request (HttpRequest): The HTTP request sent by the user.
            - args (list): Optional arguments.
            - kwargs (dict): Optional keyword arguments.
        Returns:
            - Response (HttpResponse): A response containing a message and status code.
        Processing Logic:
            - Validate the serializer data.
            - Retrieve the validated user data.
            - Create or return a token.
            - Return a response with a success message and status code if valid, or errors and status code if invalid."""
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            # Assuming you have some mechanism to create or return a token
            return Response({"message": "Login successful"}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)