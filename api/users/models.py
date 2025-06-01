from django.db import models
from django.contrib.auth.models import AbstractUser #You inherit from AbstractUser when you want to extend or customize the built-in User model but still keep its default fields (like first_name, last_name, password, etc.).
from .managers import CustomUserManager # For overriding how users are created, methods include create_user and create_superuser

# Create your models here.
class CustomUser(AbstractUser): # model inherits everything in the default user model, but you can override or add new fields/behavior
    USERNAME_FIELD = 'email' # Tells django to use the username as the unique identifier
    email = models.EmailField(unique=True)
    REQUIRED_FIELDS = [] # Fields prompted by django when creating a new superuser

    objects = CustomUserManager()