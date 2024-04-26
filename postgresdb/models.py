from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
class Category(models.Model):
    category = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.category

class Item(models.Model):
    sku = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = ArrayField(models.CharField(max_length=50, blank=True), default=list, blank=True)
    inStock = models.IntegerField()
    availableStock = models.IntegerField()

    def __str__(self):
        return self.name

class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        """Creates a new user with the given email, username, and password.
        Parameters:
            - email (str): User's email address.
            - username (str): User's desired username.
            - password (str): User's desired password. Defaults to None.
        Returns:
            - User: Newly created user object.
        Processing Logic:
            - Raises error if email or username is missing.
            - Normalizes email address.
            - Sets password for user.
            - Saves user to database."""
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have a username")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        """Creates a superuser with given credentials.
        Parameters:
            - email (str): Email address of the user.
            - username (str): Username of the user.
            - password (str): Password of the user.
        Returns:
            - user (User): Newly created superuser.
        Processing Logic:
            - Create user with given credentials.
            - Set user as admin, staff, and superuser.
            - Save user using the default database."""
        user = self.create_user(
            email,
            password=password,
            username=username,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class UserCredentials(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=100)  # Note: Password should not be stored directly

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return self.email
