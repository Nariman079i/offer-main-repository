

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

from django.shortcuts import render ,HttpResponse
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
    username = CharField(max_length=255, allow_blank=True , allow_null=False, required=False)
    email = EmailField(max_length=255, allow_blank=True, allow_null=False)
    password = CharField(max_length=255, allow_null=False, allow_blank=True)

    class Meta:
        model = User
        fields = ('username', 'email','password')
        extra_kwargs = {
            'username':{'blank':True},
            'password': {'write_only': True},
            'email':{'blank':True}
        }

    def create(self, validated_data):
        if User.objects.filter(email=validated_data['email']).exists():
            raise ValidationError({"username":["Пользователь с такой почтой уже существует"]})


        user = User(email = validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user

class UserSerializerPass(ModelSerializer):
    class Meta:
        model = User
        fields = ('username' , 'email')


class InvestorSerializerList(ModelSerializer):
    user = UserSerializerPass(read_only=True)

    class Meta:
        model = Investor
        fields = '__all__'

class CompanySerializerList(ModelSerializer):
    user = UserSerializerPass(read_only=True)

    class Meta:
        model = Company
        fields = '__all__'

class BussinessmenSerializerList(ModelSerializer):
    user = UserSerializerPass(read_only=True)

    class Meta:
        model = Bussinessmen
        fields = '__all__'


class InvestorSerializer(ModelSerializer):
    user = HiddenField(default=CurrentUserDefault())

    class Meta:
        model = Investor
        fields = '__all__'

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
            return Response({'error':['Неправильно введен пароль']})

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

class CreateBussinessmen(ListAPIView):
    queryset = Bussinessmen
    serializer_class = BussinessmenSerializer

    permission_classes = (IsAuthenticated)


class InvestorListAPI(ListAPIView):
    queryset = Investor.objects.all()
    serializer_class = InvestorSerializerList

    permission_classes = (AllowAny,)

class CompanyListAPI(ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializerList

    permission_classes = (AllowAny,)

class BussinessmenListAPI(ListAPIView):
    queryset = Bussinessmen.objects.all()
    serializer_class = BussinessmenSerializerList

    permission_classes = (AllowAny,)

class CompanyEditAPI(ListAPIView,UpdateAPIView):
    serializer_class = CompanySerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        return Company.objects.filter(pk=pk)

    permission_classes = (IsAuthenticated,)



