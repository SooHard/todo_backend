from django.urls import path, include
from rest_framework.routers import SimpleRouter
from todo.views import TodoViewSet

app_name = 'todo'

router = SimpleRouter()
router.register('', TodoViewSet, basename='todo')

urlpatterns = [
    path('', include(router.urls)),
]