from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from django.shortcuts import render
from django.core.validators import EmailValidator
from rest_framework.authtoken.models import Token
from rest_framework.generics import *
from rest_framework.response import Response
from rest_framework.serializers import *
from rest_framework.views import APIView
from rest_framework.permissions import *
# Create your views here.
from offer_start.models import Investor , Bussinessmen, Company

#Seiralizer Start Line !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

class UserSerializer(ModelSerializer):
    username = CharField(max_length=255, allow_blank=True , allow_null=False)
    email = EmailField(
        max_length=255,
        allow_blank=True,
        allow_null=False,
        validators=[EmailValidator(message="Недействительный адрес почты", code="invalid"),]
    )

    password = CharField(max_length=255, allow_null=False, allow_blank=True)
    class Meta:
        model = User
        fields = ('username', 'email','password')
        extra_kwargs = {
            'username':{'blank':True},
            'password': {'write_only': True},
            'email':{'blank':True}
        }

    def validate_username(self, value):
        if len(value) == 0:
            raise ValidationError('Поле не может быть пустым')
        return value

    def validate_email(self, value):
        if len(value) == 0:
            raise ValidationError('Поле не может быть пустым')
        if "@" not in value:
            raise ValidationError("Недействительный адрес")
        return value
    def validate_password(self, value):
        if len(value) == 0:
            raise ValidationError('Поле не может быть пустым')
        return value

    def create(self, validated_data):
        if User.objects.filter(username=validated_data['username']).exists():
            raise ValidationError({"username":"Пользователя с таким именем уже существует"})


        user = User(
            email = validated_data['email'],
            username = validated_data['username']
                    )
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user



class InvestorSerializer(ModelSerializer):
    user = HiddenField(default=CurrentUserDefault())

    class Meta:
        model = Investor
        fields = '__all__'


    def validate_inn(self, value):
        if len(value) > 12:
            raise ValidationError('Длина поля не может быть больше 12 чисел')
        if len(value) == 0:
            raise ValidationError('Поле не может быть пустым')
        try :
            for i in value:
                с = int(i)
                print(с)
        except:
            raise ValidationError('Поле должно состоять только из цифр')
        return value

    def validate_call_number(self, value):
        if len(value) > 12:
            raise ValidationError('Длина поля не может быть больше 12 чисел')
        if len(value) == 0:
            raise ValidationError('Поле не может быть пустым')
        try :
            for i in value:
                с = int(i)
                print(с)
        except:
            raise ValidationError('Поле должно состоять только из цифр')
        return value


class BussinessmenSerializer(ModelSerializer):
    user = HiddenField(default=CurrentUserDefault())

    class Meta:
        model = Bussinessmen
        fields = '__all__'

class CompanySerializer(ModelSerializer):
    user = HiddenField(default=CurrentUserDefault())

    class Meta:
        model = Company
        fields = '__all__'

#Serializers End line !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


class UserGetToken(APIView):
    def post(self,request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(
            username=username,
            password=password
                            )
        if user:
            return Response({
                'auth_token':user.auth_token.key
            })
        else:
            return Response({'error':'error'})

#Views Start Line !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
class CreateBussinessmen(CreateAPIView):
    queryset = Bussinessmen.objects.all()
    serializer_class = BussinessmenSerializer

    permission_classes = (IsAuthenticated,)

class CreateCompany(CreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    permission_classes = (IsAuthenticated,)

class CreateInvestor(CreateAPIView):
    queryset = Investor.objects.all()
    serializer_class = InvestorSerializer

    permission_classes = (IsAuthenticated,)

