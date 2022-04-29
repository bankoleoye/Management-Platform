from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager


# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        """
        Creates and saves a new user
        """
        if not email:
            raise ValueError('Email must be set!')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        print(password)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Creates and save a super user with the given email and password.
        """
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_admin', True)
        extra_fields.setdefault('duties', 'CEO')
        if extra_fields.get('is_staff') is not True:
            raise ValueError(('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    """
    Creates user model that supports the use of email instead of username
    """
    DUTIES = (
        ('Community manager', 'Community manager'),
        ('Accountant', 'Accountant'),
        ('IT Support', 'IT Support'),
        ('Admin', 'Admin'),
        ('CEO', 'CEO'),
    ) 


    duties = models.CharField(choices=DUTIES, max_length=29, default='user')
    mobile_number = models.CharField(max_length=15, unique=True, default=0)
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class Sessions(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=70)
    date = models.DateTimeField()
    booking_date = models.DateTimeField(auto_now_add=True)
    is_booked = models.BooleanField(default=False)
    description = models.CharField(max_length=255, default=False)

    def __str__(self):
        return self.title


class Ticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=70)
    description = models.CharField(max_length=255, default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Subscription(models.Model):
    PLANS = (
        ('Basic', 'Basic'),
        ('Premium', 'Premium')
    )

    title = models.CharField(max_length=70)
    package = models.CharField(max_length=70)
    price = models.CharField(max_length=20)
    plans = models.CharField(choices=PLANS, max_length= 29, default='basic')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

def __str__(self):
    return self.title

class NewsLetter(models.Model):
    title = models.CharField(max_length=40, null=True)
    topic = models.CharField(max_length=90, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title
