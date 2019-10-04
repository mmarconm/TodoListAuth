from django.db import models


class TodoList(models.Model):

    title = models.CharField(max_length=100)
    isCompleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at', )
