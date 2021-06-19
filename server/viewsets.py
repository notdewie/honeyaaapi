from django.db.models import query
from rest_framework import viewsets

from .models import Interest, Oriented, Person, Picture, SwipePerson
from .serializers import InterestSerializer, PersonSerializer, PictureSerializer, SwipePersonSerializer, OrientedSerializer
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