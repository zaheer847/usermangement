from rest_framework import serializers
from .models import Product, UserProfile

class ProductSerializer(serializers.ModelSerializer):
    """
    Serializer for the Product model.

    This serializer is used to serialize Product objects for API responses.

    Meta:
    - model: The Product model to be serialized.
    - fields: The fields to include in the serialization (all fields in this case).
    """
    class Meta:
        model = Product
        fields = '__all__'

class UserProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for the UserProfile model.

    This serializer is used to serialize UserProfile objects for API responses.

    Meta:
    - model: The UserProfile model to be serialized.
    - fields: The fields to include in the serialization (profile_picture and bio).
    """
    class Meta:
        model = UserProfile
        fields = ('profile_picture', 'bio')

