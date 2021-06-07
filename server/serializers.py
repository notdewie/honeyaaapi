from django.db import models
from rest_framework import serializers

from .models import User
# from .models import Players

# class PlayersSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Players
#         fields = '__all__'

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= User
        fields = ('userName', 'userPassword')