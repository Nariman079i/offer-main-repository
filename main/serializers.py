from rest_framework.serializers import *
from main.models import *
from django.contrib.auth.models import User


class UserSerializer(ModelSerializer):
    role = CharField(max_length=30)
    class Meta:
        model = User
        fields = ('username', 'email','password')

class TestSerializer(ModelSerializer):

    user = HiddenField(default=CurrentUserDefault())

    class Meta:
        model = TestProfile
        fields = ('user','img', 'first_name', 'last_name', 'industry','locate','status', 'role')


class ProfileSerialiser(ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id','img', 'first_name', 'last_name', 'industry','locate','status', 'role')


