from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('', views.home, name='home'),
    path('contact-us/', views.contact, name='contact'),
    path('api/get-jwt-token', views.get_jwt_token, name='jwtToken'), # Generate JWT token
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Generate JWT token
    path('signup/', views.signup, name='signup'),  # User registration
    path('login/', auth_views.LoginView.as_view(), name='login'),  # Built-in login view
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),  # Logout and redirect to home
    path('accounts/profile/', views.profile, name='profile'),  # User profile page
]
