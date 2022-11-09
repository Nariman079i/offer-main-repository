from rest_framework.serializers import ModelSerializer
from main.models import *
from django.contrib.auth.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username','email','password',)

class ProfileSerialiser(ModelSerializer):
    class Meta:
        model = Profile
        fields = ('img', 'first_name', 'last_name', 'industry','locate','status', 'role')
