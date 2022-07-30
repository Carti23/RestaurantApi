from django.shortcuts import render
from .serializers import RegisterSerializer, MyTokenObtainPairSerializer, EmployeeSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import *
from rest_framework import generics, views
from django.contrib.auth.models import User


# Register Api View
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


# Login Api View
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


# Employee List API View
class EmployeeListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = EmployeeSerializer
