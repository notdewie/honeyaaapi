# from server.viewsets import PlayerViewSet
from server.viewsets import UserViewSet
from rest_framework import routers

router = routers.DefaultRouter()
# router.register('players', PlayerViewSet)
router.register('user', UserViewSet)

#localhost:p/api/players