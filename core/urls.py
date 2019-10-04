from rest_framework import routers
from core.views import TodoListViewSet

router = routers.DefaultRouter()

router.register('todos', TodoListViewSet)

urlpatterns = router.urls
