# from rest_framework import serializers
# from .models import User

# class RegisterSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(max_length = 30, min_length=6, write_only=True)

#     class Meta:
#         model = User
#         fields = ['email', 'username', 'password']

#     def validate(self, attrs):
#         email = attrs.get('email', '')
#         username = attrs.get('username', '')
#         if not username.isalnum():
#             raise serializers.ValidationError('The username should be alphanumeric characters')
#         return attrs
        
#     def create(self, validated_data):
#         return User.objects.create_user(**validated_data)

# class EmailVerification(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['otp', 'email']

# class LoginSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(max_length=20, min_length=6, write_only=True)
#     class Meta:
#         model = User
#         fields = ['email', 'password']

# class ForgetPasswordSerializer(serializers.ModelSerializer):
#     email = serializers.EmailField(min_length=2)
#     class Meta:
#         model = User
#         fields=['email']

# class ResetPasswordSerializer(serializers.ModelSerializer):
#     confrim_password = serializers.CharField(min_length=8)
#     class Meta:
#         model = User
#         fields = ['confirm_password']
