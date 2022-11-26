
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from offer_start.views import *
from Offer import settings

urlpatterns = [
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

