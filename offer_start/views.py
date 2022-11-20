from django.shortcuts import render
from rest_framework.generics import *
from rest_framework.serializers import *
from rest_framework.permissions import *
# Create your views here.
from offer_start.models import Investor , Bussinessmen, Company

#Seiralizer Start Line !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
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

