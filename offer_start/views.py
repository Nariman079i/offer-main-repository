from rest_framework.generics import CreateAPIView
from rest_framework.viewsets import GenericViewSet

from offer_start.serializers import *
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
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
    queryset = Bussinessmen.objects.all()

    permission_classes = (IsAuthenticated,)

class CreateCompany(mixins.CreateModelMixin,
                    mixins.UpdateModelMixin,
                    GenericViewSet):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()
"""
Исправить ошибку с Bussinessmen
"""