from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserProfileViewSet, MessageViewSet

router = DefaultRouter()
router.register(r'userprofiles', UserProfileViewSet)
router.register(r'messages', MessageViewSet)

urlpatterns = router.urls  # Use router.urls directly
