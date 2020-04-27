from django.shortcuts import render
from .serializer import UserSerializer
from rest_framework.generics import CreateAPIView


class RegisterAPI(CreateAPIView):
	serializer_class = UserSerializer
