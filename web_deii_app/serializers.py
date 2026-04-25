from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])


#class LoginSerializer(serializers.ModelSerializer):

#    class Meta:
#        model = User
#        fields = ['username', 'password']
#        extra_kwargs = {'password': {'write_only': True, 'required': True}}