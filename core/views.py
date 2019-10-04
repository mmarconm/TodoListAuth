from rest_framework import viewsets
from core.models import TodoList
from core.serializers import TodoListSerializer


class TodoListViewSet(viewsets.ModelViewSet):

    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer
