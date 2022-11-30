
from rest_framework.serializers import *
from offer_start.models import *
from users.serializers import UserSerializer


class ProfileInvestorSerializer(ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Investor
        fields = ('user','name','surname','avatar')

class InvestorSerializer(ModelSerializer):
    user = HiddenField(default=CurrentUserDefault())
    class Meta:
        model = Investor
        fields = '__all__'

class BusinessmanSerializer(ModelSerializer):
    user = HiddenField(default=CurrentUserDefault())
    class Meta:
        model = Businessman
        fields = "__all__"

class CompanySerializer(ModelSerializer):
    user = HiddenField(default=CurrentUserDefault())
    class Meta:
        model = Company
        fields = '__all__'