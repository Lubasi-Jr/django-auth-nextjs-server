from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateAPIView, CreateAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .serializers import CustomUserSerializer, RegisterUserSerializer, LoginUserSerializer

# Create your views here
class UserInfoView(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated)
    serializer_class = CustomUserSerializer

    def get_object(self): # Tells DRF which object to retrieve or update
        return self.request.user

class UserRegistrationView(CreateAPIView):
    serializer_class = RegisterUserSerializer

class LoginView(APIView):
    def post(self,request):
        serializer = LoginUserSerializer(data= request.data)

        # Generate JWT token

