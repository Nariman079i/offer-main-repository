from django.shortcuts import render
from rest_framework.serializers import *
from rest_framework.generics import *
from todoapp.models import Task
from rest_framework.permissions import IsAuthenticated
class TaskSerialiser(ModelSerializer):
    user = HiddenField(default=CurrentUserDefault())
    class Meta:
        model = Task
        fields = "__all__"

class TaskListApi(ListAPIView,CreateAPIView):
    serializer_class = TaskSerialiser
    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


    permission_classes = (IsAuthenticated,)