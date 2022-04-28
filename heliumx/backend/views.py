from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, permissions
from .serializers import LoginSerializer, UserListSerializer, AdminUserSerializer, TicketSerializer, UserSerializer
from .models import User, Sessions, Ticket
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate
from .permissions import IsAuthenticated, IsCEO, IsCommunityManager, IsITSupport
from .utils import Util
from .models import Sessions, Ticket, User



# # Create your views here.

class Login(generics.GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer
    def post(self, request):
        email = request.data.get('email', '')
        password = request.data.get('password', '')
        if email is None or password is None:
            return Response(errors={'invalid_credentials': 'please provide both email and password'}, status=status.HTTP_400_BAD_REQUEST)
        user = authenticate(username=email, password=password)
        if not user:
            return Response(errors={'invalid_credentials': 'Ensure both email and password are correct and you have verified your account'}, status=status.HTTP_400_BAD_REQUEST)


