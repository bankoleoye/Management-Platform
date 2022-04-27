from dataclasses import fields
from rest_framework import serializers
from .models import User, Sessions, Ticket

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password', 'duties']

class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=20, min_length=6, write_only=True)
    class Meta:
        model = User
        fields = ['email', 'password']

class AdminUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length = 64, min_length = 6, write_only = True)
    duties = serializers.ChoiceField(choices=User.DUTIES)
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'mobile_number', 'duties']

class NewsLetter(serializers.Serializer):
    title = serializers.CharField(max_length=70)
    body = serializers.CharField()
    class Meta:
        model = User
        fields = ['title', 'body']

class SessionSerializer(serializers.ModelSerializer):
    users = serializers.PrimaryKeyRelatedField(many=True, queryset=User.objects.all())
    class Meta:
        model = Sessions
        fields = ['users', 'session_date', 'is_booked', 'title']

class TicketSerializer(serializers.ModelSerializer):
    users = serializers.PrimaryKeyRelatedField(many=True, queryset=User.objects.all())
    class Meta:
        model = Ticket
        fields = ['users', 'ticket_title', 'ticket_description']

class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        mdoel = User
        fields = ['first_name', 'last_name', 'username', 'email', 'duties']

class UserPlansSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'plans']