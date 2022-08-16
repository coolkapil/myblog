from pyexpat import model
from .models import Post
from rest_framework import serializers
from django.contrib.auth.models import User



class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields ='__all__'


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff', 'is_superuser', 'password']