from django.urls import path
from main.views import *

urlpatterns = [
    path('', index),
    path('api/v1/inn/<str:inn>/', get_inn_user)
]