from rest_framework import serializers
from ..models import Todo
from django.contrib.auth.models import User
from django.http import request

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id','user', 'description', 'date']


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email = validated_data['email'],
            password=validated_data['password'],
        )
        return user


        