from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator
from .models import *
from rest_framework import serializers
from django.forms import ModelForm
from django.contrib.auth.models import User

class AllDomainSerializer(serializers.ModelSerializer):
    class Meta:
        model = AllDomain
        fields = '__all__'
