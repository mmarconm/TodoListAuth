from django.contrib import admin

from core.models import TodoList


@admin.register(TodoList)
class TodoListAdmin(admin.ModelAdmin):
    list_display = ('title', 'isCompleted', 'created_at', 'updated_at', )
