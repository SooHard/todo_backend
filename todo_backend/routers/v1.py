from django.urls import path, include

app_name = 'v1'

urlpatterns = [
    path('todo/', include('todo.urls.v1')),
]