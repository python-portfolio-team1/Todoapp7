from todoapp.viewsets import ToDoViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('todo', ToDoViewset)