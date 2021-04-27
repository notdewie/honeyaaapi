from rest_framework import viewsets
from . import models
from . import serializers

class PlayerViewSet(viewsets.ModelViewSet):
    queryset = models.Players.objects.all()
    serializer_class = serializers.PlayersSerializer
    