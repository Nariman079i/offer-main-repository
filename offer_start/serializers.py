from rest_framework.authtoken.models import Token
from rest_framework.serializers import *
from offer_start.models import *
from users.models import CustomUser
from djoser.serializers import UserCreateSerializer

User = CustomUser


class UserSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('email','password')

    def create(self, validated_data):
        email = validated_data.get('email')
        password = validated_data.get('password')
        user = User.objects.create_user(email=email)
        user.set_password(password)
        user.save()
        Token.objects.create(user=user)
        return user

class InvestorSerializer(ModelSerializer):
    user = HiddenField(default=CurrentUserDefault())
    class Meta:
        model = Investor
        fields = '__all__'

class BusinessmanSerializer(ModelSerializer):
    user = HiddenField(default=CurrentUserDefault())
    class Meta:
        model = Bussinessmen
        fields = "__all__"

class CompanySerializer(ModelSerializer):
    user = HiddenField(default=CurrentUserDefault())
    class Meta:
        model = Company
        fields = '__all__'