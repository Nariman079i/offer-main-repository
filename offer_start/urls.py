
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from offer_start.views import *
from Offer import settings

urlpatterns = [
    path('create/user/inv/',CreateInvestor.as_view()),
    path('create/user/bus/',CreateBussinessmen.as_view()),
    path('create/user/com/',CreateCompany.as_view()),
    path('list/inv/', InvestorListAPI.as_view()),
    path('list/com/', CompanyListAPI.as_view()),
    path('get/token/', UserGetToken.as_view()),
    path('auth/', include('djoser.urls')),
    re_path('auth/', include('djoser.urls.authtoken'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

