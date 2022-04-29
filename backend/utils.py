from django.core.mail import EmailMessage
import string
from random import random


class Util:
    @staticmethod
    def send_mail(data):
        email = EmailMessage(
            subject = data['email_subject'], body = data['email_topic'], to = [data['to_email']])
        email.send()

# class Util:
#     @staticmethod
#     def create_password(num):
#         return '007'+ ''.join(random.choice(string.digits) for i in range(num))
