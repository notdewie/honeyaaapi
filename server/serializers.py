from django.core.exceptions import FieldDoesNotExist
from django.db import models
from django.db.models import fields
from rest_framework import serializers

from .models import Interest, Person, Picture, SwipePerson, Oriented
# from .models import Players

# class PlayersSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Players
#         fields = '__all__'

# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model= User
#         fields = ('userName', 'userPassword')

class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'

class SwipePersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SwipePerson
        fields = '__all__'

class OrientedSerializer( serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Oriented
        fields = '__all__'

class InterestSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Interest
        fields = '__all__'

class PictureSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Picture
        fields = '__all__'