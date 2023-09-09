from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    """
    Model for representing products in the online store.

    Fields:
    - name: Product name (up to 100 characters).
    - category: Product category (up to 100 characters).
    - description: Product description (text).
    - price: Product price (up to 10 digits with 2 decimal places).
    """
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

class UserProfile(models.Model):
    """
    Model for storing user profile information.

    Fields:
    - user: One-to-One relationship with the User model from Django's built-in auth system.
    - profile_picture: User's profile picture (uploaded to 'profile_pictures/' directory).
    - bio: User's biography (text, optional).
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    bio = models.TextField(blank=True)
