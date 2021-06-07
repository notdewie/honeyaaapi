# from server.viewsets import PlayerViewSet
from server.models import Oriented
from server.viewsets import InterestViewSet, OrientedViewSet, PersonViewSet, SwipePersonViewSet, UserViewSet
from rest_framework import routers

router = routers.DefaultRouter()
# localhost : p/api/user
router.register('user', UserViewSet)
router.register('person', PersonViewSet)
router.register('swipeperson', SwipePersonViewSet)
router.register('oriented', OrientedViewSet)
router.register('interest', InterestViewSet)
# router.register('players', PlayerViewSet)
#localhost:p/api/players