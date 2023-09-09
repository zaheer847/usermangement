from django.contrib.auth.forms import UserCreationForm, User, UserChangeForm
from django import forms
from .models import UserProfile

class CustomUserCreationForm(UserCreationForm):
    """
    Custom user creation form with additional fields.

    This form extends the UserCreationForm and adds fields for user permissions.

    Fields:
    - is_superuser: Checkbox for superuser permission.
    - is_staff: Checkbox for staff permission.
    - is_active: Checkbox for account activation status.

    Inherits from:
    - UserCreationForm: The base user creation form.

    Meta:
    - model: The User model from django.contrib.auth.
    - fields: Fields to include, including the custom fields.
    """
    is_superuser = forms.BooleanField(initial=False, required=False, widget=forms.HiddenInput)
    is_staff = forms.BooleanField(initial=True, required=False, widget=forms.HiddenInput)
    is_active = forms.BooleanField(initial=True, required=False, widget=forms.HiddenInput)

    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('is_superuser', 'is_staff', 'is_active')

class UserProfileForm(forms.ModelForm):
    """
    Form for updating user profile information.

    Fields:
    - profile_picture: User's profile picture.
    - bio: User's biography.

    Meta:
    - model: The UserProfile model from the current app.
    - fields: Fields to include in the form.
    """
    class Meta:
        model = UserProfile
        fields = ['profile_picture', 'bio']

class UserUpdateForm(UserChangeForm):
    """
    Form for updating user information.

    Fields:
    - first_name: User's first name.
    - last_name: User's last name.
    - email: User's email address.
    - username: User's username.

    Meta:
    - model: The User model from django.contrib.auth.
    - fields: Fields to include in the form.
    """
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username']

class ContactForm(forms.Form):
    """
    Contact form for sending messages.

    Fields:
    - name: Sender's name.
    - email: Sender's email address.
    - subject: Message subject.
    - message: Message content (textarea).
    """
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
