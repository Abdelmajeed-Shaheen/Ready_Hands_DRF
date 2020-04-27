from django.urls import path
from .views import RegisterAPI
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('register', RegisterAPI.as_view(), name='api-register'),
    path('login', TokenObtainPairView.as_view(), name='api-login'),
    ]
