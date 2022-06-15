from rest_framework import viewsets
from . import models
from . import serializers


class ToDoViewset(viewsets.ModelViewSet):
    queryset = models.ToDo.objects.all()
    serializer_class = serializers.ToDoSerializers