from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils import timezone


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
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Creates and save a super user with the given email and password.
        """
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_admin', True)
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
    ) 

    PLANS = (
        ('Basic', 'Basic'),
        ('Premium', 'premium'),
    )

    duties = models.CharField(choices=DUTIES, max_length=29, default='user')
    plans = models.CharField(choices=PLANS, max_length= 29, default='basic')
    mobile_number = models.CharField(max_length=10, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=False, default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_IT_support = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_CEO = models.BooleanField(default=False)
    is_accountant = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class Sessions(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    session_title = models.CharField(max_length=70)
    session_date = models.DateTimeField(auto_now_add=True)
    booking_date = models.DateTimeField(auto_now_add=True)
    is_booked = models.BooleanField(default=False)

    def __str__(self):
        return self.session_title


class Ticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ticket_title = models.CharField(max_length=70)
    ticket_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.ticket_title
