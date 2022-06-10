from todo.models import Todo
from rest_framework import serializers


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = [
            'title', 'description', 'is_done',
            'deadline', 'created_at', 'updated_at',
        ]


