from server.viewsets import PlayerViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('players', PlayerViewSet)

#localhost:p/api/players