from django.db import models
from datetime import datetime    
from django.contrib.auth.models import AbstractUser 
from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail


# Create your models here.

class User(AbstractUser):

    '''''
    extended the User model of django to store additional info 
    '''''

    phone = models.CharField(unique=True, max_length=31, null=True, blank=True)
    secret_question = models.CharField(unique=True, max_length=31, null=True, blank=True)
    secret_answer = models.CharField(unique=True, max_length=31, null=True, blank=True)

    class Meta:
        unique_together = ['phone']


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    send_mail(
        # title:
        "Password Reset for {title}".format(title="Some website title"),
        # message:
        'The token to reset your password is {}. \nPut the token in the next window'.format(reset_password_token.key),
        # from:
        "noreply@somehost.local",
        # to:
        [reset_password_token.user.email]
    )



