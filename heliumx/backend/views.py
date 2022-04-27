# from django.shortcuts import render
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status, generics, permissions
# from .serializers import RegisterSerializer, LoginSerializer, ResetPasswordSerializer
# from .models import User
# from rest_framework.permissions import AllowAny
# from django.contrib.auth import authenticate, logout
# from django.core.exceptions import ObjectDoesNotExist


# # Create your views here.
# class RegisterView(generics.GenericAPIView):
#     permission_classes = [AllowAny]
#     serializer_class = RegisterSerializer

#     def post(self, request):
#         user = request.data
#         serializer = self.serializer_class(data=user)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         user_data = serializer.data
#         user = User.objects.get(email = user_data['email'])

# class Login(generics.GenericAPIView):
#     permission_classes = [AllowAny]
#     serializer_class = LoginSerializer
#     def post(self, request):
#         email = request.data.get('email', '')
#         password = request.data.get('password', '')
#         if email is None or password is None:
#             return Response(errors={'invalid_credentials': 'please provide both email and password'}, status=status.HTTP_400_BAD_REQUEST)
#         user = authenticate(username=email, password=password)
#         if not user:
#             return Response(errors={'invalid_credentials': 'Ensure both email and password are correct and you have verified your account'}, status=status.HTTP_400_BAD_REQUEST)

# class Logout(generics.GenericAPIView):
#     def get(self, request):
#         logout(request)
#         return Response(status=status.HTTP_200_OK)

# class PasswordReset(generics.GenericAPIView):
#     serializer_class = ResetPasswordSerializer

#     def put(self, request):
#         serializer=self.serializer_class(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         email = serializer.data.get('email')
#         password = request.data.get('password')
#         confirm_password = request.data.get('confirm_password')
#         try:
#             user = User.objects.get(email=email)
#         except ObjectDoesNotExist:
#             return Response({"message":"User does not exist"}, status=404)
