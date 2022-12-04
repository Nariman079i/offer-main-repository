
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

    def validate(self,data):
        errors = {}
        text = 'Поле не должно быть пустым'
        for k in data:
            if not data[k] or data[k] == "":
                errors[k] = text
                raise ValidationError({k:text})
        return data

class BusinessmanSerializer(ModelSerializer):
    user = HiddenField(default=CurrentUserDefault())
    class Meta:
        model = Businessman
        fields = "__all__"

    def validate(self, data):
        errors = {}
        text = 'Поле не должно быть пустым'
        for k in data:
            if not data[k] or data[k] == "":
                errors[k] = text
                raise ValidationError({k: text})
        return data

class CompanySerializer(ModelSerializer):
    user = HiddenField(default=CurrentUserDefault())
    class Meta:
        model = Company
        fields = '__all__'

    def validate(self,data):
        errors = {}
        text = 'Поле не должно быть пустым'
        for k in data:
            if not data[k] or data[k] == "":
                errors[k] = text
                raise ValidationError({k:text})
        return data