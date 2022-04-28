from unicodedata import name
from django.urls import path
from .views import *

urlpatterns = [
    path('register', CeoRegisterUser.as_view(), name='register'),
    path('login', Login.as_view(), name='login'),
    path('subscribe', CreateSubscription.as_view(), name='subscribe'),
    path('user/subscribe/<int:pk>', UpdateSubscription.as_view(), name='subscribe'),
    path('ticket', CreateTickets.as_view(), name='ticket'),
    path('ticket/<int:pk>', UpdateTickets.as_view(), name='ticket'),
    path('sessions', CreateSession.as_view(), name='sessions'),
    path('sessions/<int:pk>', UpdateSession.as_view(), name='sessions'),
    path('newsletter', SendNewsLetter.as_view(), name='newsletter'),
    path('sign-up', RegisterUsers.as_view(), name='sign-up'),
    path('user/communityManager/<int:pk>', UpdateUserByCommunityManager.as_view(), name='user'),
    path('user/update/<int:pk>', CeoUpdateUser.as_view(), name='user'),
    path('user/<int:pk>', UpdateUserByCommunityManager.as_view(), name='user'),
    path('user_view', ViewAllUsers.as_view(), name='user'),
]
