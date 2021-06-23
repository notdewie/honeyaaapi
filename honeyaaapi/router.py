# from server.viewsets import PlayerViewSet
from django.conf.urls import url
from server.viewsets import InterestViewSet, OrientedViewSet, PersonViewSet, PictureViewSet, SwipePersonViewSet
from rest_framework import routers

router = routers.DefaultRouter()
# localhost : p/api/user
# router.register('user', UserViewSet)
router.register('person', PersonViewSet)
router.register('swipeperson', SwipePersonViewSet)
router.register('oriented', OrientedViewSet)
router.register('interest', InterestViewSet)
router.register('picture', PictureViewSet)

# urlpatterns = [
#     url(r'^', include(router.urls)),
# ]
# router.register('players', PlayerViewSet)
#localhost:p/api/players