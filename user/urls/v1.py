from django.urls import path, include
from rest_framework.routers import SimpleRouter

from user.views import ReadOnlyUserViewSet

app_name = 'user'

router = SimpleRouter()
router.register('', ReadOnlyUserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
]