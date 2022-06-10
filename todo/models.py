from django.db import models
from user.models import User


class Todo(models.Model):
    title = models.CharField(unique=True, max_length=50)
    description = models.TextField(max_length=255)
    is_done = models.BooleanField(default=False)
    deadline = models.DateTimeField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='todos')

    class Meta:
        verbose_name = 'Todo'
        verbose_name_plural = 'Todo list'

    def __str__(self):
        return self.title
