from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from rest_framework.generics import *
from offer_start.serializers import *
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated ,AllowAny
from offer_start.models import *

class CreateInvestor(mixins.CreateModelMixin,
                     GenericViewSet
                     ):
    serializer_class = InvestorSerializer
    queryset = Investor.objects.all()

    permission_classes = (IsAuthenticated,)

class CreateBusinessman(mixins.CreateModelMixin,
                     GenericViewSet
                     ):
    serializer_class = BusinessmanSerializer
    queryset = Businessman.objects.all()

    permission_classes = (IsAuthenticated,)

class CreateCompany(mixins.CreateModelMixin,
                    mixins.UpdateModelMixin,
                    GenericViewSet):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()

    permission_classes = (IsAuthenticated,)


class PersonAccountApi(ListAPIView):
    serializer_class = ProfileInvestorSerializer
    def get_queryset(self):
        return Investor.objects.filter(user=self.request.user)

    permission_classes = (IsAuthenticated,)


class InvestorListLimit(ListAPIView):
    def get_queryset(self):
        limit = self.kwargs.get('count')
        return Investor.objects.all()[:limit]
    serializer_class = InvestorSerializer
class InvestorList(ListAPIView):
    queryset = Investor.objects.all()
    serializer_class = InvestorSerializer

class BusinessmanListLimit(ListAPIView):
    def get_queryset(self):
        limit = self.kwargs.get('count')
        return Businessman.objects.all()[:limit]
    serializer_class = BusinessmanSerializer
class BusinessmanList(ListAPIView):
    queryset = Businessman.objects.all()
    serializer_class = BusinessmanSerializer

class CompanyListLimit(ListAPIView):
    def get_queryset(self):
        limit = self.kwargs.get('count')
        return Company.objects.all()[:limit]
    serializer_class = CompanySerializer

class CompanyList(ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer