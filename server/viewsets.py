from typing import List
from django.db.models import query
from django.http import response
import json
from django.core import serializers as core_serializers
from django.http.response import HttpResponse, JsonResponse
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.serializers import ListSerializer

from .models import Interest, OneSignal, Oriented, Person, Picture, SwipePerson
from .serializers import InterestSerializer, OneSignalSerializer, PersonSerializer, PictureSerializer, SwipePersonSerializer, OrientedSerializer
from server import serializers

# class PlayerViewSet(viewsets.ModelViewSet):
#     queryset = models.Players.objects.all()
#     serializer_class = serializers.PlayersSerializer

# class UserViewSet (viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    # lookup_field = 'uid'

    # @action(detail=True, methods=['get'])
    # def get(self, request, pk = None):
    #     data = list(Person.objects.values())
    #     # queryset = Person.objects.all()
    #     # query_json = core_serializers.serialize('json', queryset)

    #     return JsonResponse(data, safe=False)
    #     # return HttpResponse(query_json, content_type='application/json')
    # @action(detail=True, methods=['get'])
    # def get_queryset(self):
    #     user = self.request.user
    #     return Person.objects.filter(user=user)

class OnesignalViewSet(viewsets.ModelViewSet):
    queryset = OneSignal.objects.all()
    serializers_class = OneSignalSerializer
 
class SwipePersonViewSet(viewsets.ModelViewSet):
    queryset = SwipePerson.objects.all()
    serializer_class = SwipePersonSerializer

class OrientedViewSet(viewsets.ModelViewSet):
    queryset = Oriented.objects.all()
    serializer_class = OrientedSerializer

class InterestViewSet(viewsets.ModelViewSet):
    queryset = Interest.objects.all()
    serializer_class = InterestSerializer

class PictureViewSet(viewsets.ModelViewSet):
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer