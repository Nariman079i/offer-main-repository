

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.generics import *
from rest_framework.response import Response
from rest_framework.serializers import *
from rest_framework.views import APIView
from rest_framework.permissions import *
from users.models import *
from djoser.serializers import UserCreateSerializer
# Create your views here.
from offer_start.models import Investor , Bussinessmen, Company

User = CustomUser
#Seiralizer Start Line !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

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


class UserSerializerPass(ModelSerializer):
    class Meta:
        model = User
        fields = ( 'email',)


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



