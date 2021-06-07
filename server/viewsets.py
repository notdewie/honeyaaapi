from rest_framework import viewsets

from .models import User
from .serializers import UserSerializer
from server import serializers

# class PlayerViewSet(viewsets.ModelViewSet):
#     queryset = models.Players.objects.all()
#     serializer_class = serializers.PlayersSerializer

class UserViewSet (viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer