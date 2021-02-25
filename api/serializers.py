from core.models import Profile
from rest_framework import serializers
from django.contrib.auth.models import User


class ProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model = Profile
		fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password')


class UpdateUserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = (
            'username',
            'first_name', 
            'last_name', 
            'email'
            )
