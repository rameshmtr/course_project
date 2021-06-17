#---------------django imports---------------
from django.db.models import fields

#---------------Models imports----------------
from .models import User

#---------------restframeworks imports----------------
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username','email', 'first_name', 'last_name', 'secret_question', 'secret_answer', 'phone']


class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'username','secret_question', 'secret_answer', 'phone']