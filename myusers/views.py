from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework_simplejwt.authentication import JWTAuthentication, JWTStatelessUserAuthentication
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout, login as auth_login
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm, UserUpdateForm, ContactForm
from .models import UserProfile, Product
from .serializers import ProductSerializer, UserProfileSerializer
from django.http import JsonResponse
from django.contrib.auth.models import AnonymousUser
from rest_framework.permissions import AllowAny
from rest_framework.authentication import SessionAuthentication

@api_view(['GET'])
@permission_classes([AllowAny])
def get_jwt_token(request):
    """
    Generates a JWT token for the authenticated user or an anonymous user.

    Parameters:
    - request: The HTTP request object.

    Returns:
    - Response: JSON response containing the JWT token.
    """
    user = request.user

    if user and user.is_authenticated:
        token = AccessToken.for_user(user)
        return Response({'token': str(token)})
    else:
        anonymous_user = AnonymousUser()
        token = AccessToken.for_user(anonymous_user)
        return Response({'token': str(token)})

@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
@authentication_classes([JWTStatelessUserAuthentication])
def contact(request):
    """
    Handles contact form submissions.

    Parameters:
    - request: The HTTP request object.

    Returns:
    - Response: JSON response with a success message or an error message.
    """
    if request.method == 'POST':
        form = ContactForm(request.data)
        if form.is_valid():
            # Process the form data and send the message (e.g., via email or other method)
            return Response({'message': 'Your message has been sent successfully!'})
        else:
            return Response({'message': 'Some authentication issue'})

    else:
        form = ContactForm()
        return render(request, 'contact.html', {'form': form})

def signup(request):
    """
    Handles user registration.

    Parameters:
    - request: The HTTP request object.

    Returns:
    - Rendered registration form or redirects to the login page.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'registration/signup.html', {'form': form})

def login(request):
    """
    Handles user login.

    Parameters:
    - request: The HTTP request object.

    Returns:
    - Rendered login form or redirects to a different page after successful login.
    """
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()

    return render(request, 'registration/login.html', {'form': form})

def logout_view(request):
    """
    Logs the user out and redirects to the home page.

    Parameters:
    - request: The HTTP request object.

    Returns:
    - Redirects to the home page.
    """
    logout(request)
    return redirect('home')

def home(request):
    """
    Renders the home page with a list of products.

    Parameters:
    - request: The HTTP request object.

    Returns:
    - Rendered home page with product data.
    """
    products = Product.objects.all()
    product_serializer = ProductSerializer(products, many=True)
    return render(request, 'home.html', {'products': product_serializer.data})

@login_required
def profile(request):
    """
    Renders the user profile page and handles profile updates.

    Parameters:
    - request: The HTTP request object.

    Returns:
    - Rendered profile page with user profile data and update forms.
    """
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = UserProfileForm(instance=user_profile)
    user_profile_serializer = UserProfileSerializer(user_profile)
    return render(request, 'profile.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'user_profile_data': user_profile_serializer.data,
    })
