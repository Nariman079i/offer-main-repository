
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path , include
from todoapp.views import *

from Offer import settings

urlpatterns = [
    path('api/v1/task/' , TaskListApi.as_view())
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

