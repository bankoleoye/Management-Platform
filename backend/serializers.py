from rest_framework import serializers
from .models import User, Sessions, Ticket, Subscription, NewsLetter

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=20, min_length=6, write_only=True)
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password', 'mobile_number']

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
        fields = ['first_name', 'last_name', 'username', 'email', 'mobile_number', 'duties', 'password']

class NewsLetterSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=70)
    topic = serializers.CharField()
    class Meta:
        model = NewsLetter
        fields = ['title', 'topic']

class SessionsSerializer(serializers.ModelSerializer):
    users = serializers.PrimaryKeyRelatedField(many=True, queryset=User.objects.all())
    class Meta:
        model = Sessions
        fields = ['users', 'date', 'is_booked', 'title', 'description']

class TicketSerializer(serializers.ModelSerializer):
    users = serializers.PrimaryKeyRelatedField(many=True, queryset=User.objects.all())
    class Meta:
        model = Ticket
        fields = ['users', 'title', 'description']

class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        mdoel = User
        fields = ['first_name', 'last_name', 'username', 'email', 'duties']

class UserPlansSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'duties']
        
class SubscriptionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = "__all__"

class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ['plans',]
        