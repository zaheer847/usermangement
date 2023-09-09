from django.contrib import admin
from .models import Product
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User  # Import the User model from django.contrib.auth
from .forms import CustomUserCreationForm

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    
    def save_model(self, request, obj, form, change):
        obj.is_superuser = False
        obj.is_staff = True
        obj.is_active = True
        obj.save()

admin.site.unregister(User)  # Unregister the default User model admin
admin.site.register(User, CustomUserAdmin)  # Register the User model with the custom admin
admin.site.register(Product)
