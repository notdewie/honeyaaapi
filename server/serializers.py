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
    url = serializers.HyperlinkedIdentityField(
        view_name='person-detail',
        # lookup_field = 'uid'
    )

    class Meta:
        model = Person
        # lookup_field = 'uid'
        fields = '__all__'
        extra_kwargs = {
            'url' : {'lookup_field' : 'uid'}
        }

class GetUIDSerializer(serializers.HyperlinkedModelSerializer):
    # url = serializers.HyperlinkedIdentityField(
    #     view_name='person-detail',
    #     # lookup_field = 'uid'  
    # )

    class Meta:
        model = Person
        fields = ('id',)
        # extra_kwargs = {
        #     'url' : {'lookup_field': 'uid'}
        # }


    # def __init__(self, *args, **kwargs): 
    #     super(PersonSerializer, sefl).__init__(*args, **kwargs)
    #     request = self.context

    # def __init__(self, *args, **kwargs):
    #     super(PersonSerializer, self).__init__(*args, **kwargs)
    #     request = self.context.get("request")
    #     if request and request.query_params.get('fields'):
    #         fields = request.query_params.get('fields')
    #         if fields:
    #             fields = fields.split(',')
    #             allowed = set(fields)
    #             existing = set(self.fields.keys())
    #             for field_name in existing - allowed:
    #                 self.fields.pop(field_name)


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
        fields = ('picture',)