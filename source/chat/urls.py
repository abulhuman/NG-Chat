from rest_framework.routers import SimpleRouter

from .views.chat import MessageViewSet, RoomViewSet

router = SimpleRouter(trailing_slash=False)
router.register('rooms', RoomViewSet)
router.register('messages', MessageViewSet)

urlpatterns = router.urls
