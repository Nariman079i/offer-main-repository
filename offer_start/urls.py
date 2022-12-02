from rest_framework.routers import DefaultRouter
from django.conf.urls.static import static
from django.urls import path,include
from Offer import settings
from offer_start.views import *

user = DefaultRouter()


user.register(r'investor', CreateInvestor)
user.register(r'businessman', CreateBusinessman)
user.register(r'company', CreateCompany)

urlpatterns = [
    path('create/', include(user.urls)),
    path('create/user/', UserCreate.as_view()),
    path('person/', PersonAccountApi.as_view()),

    path('list/investor/', InvestorList.as_view()),
    path('list/investor/<int:count>/', InvestorListLimit.as_view()),

    path('list/company/', CompanyList.as_view()),
    path('list/company/<int:count>/', CompanyListLimit.as_view()),

    path('list/businessman/', BusinessmanList.as_view()),
    path('list/businessman/<int:count>/', BusinessmanListLimit.as_view()),
]
