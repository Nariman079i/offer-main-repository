from django.urls import path, include
from main.views import *

urlpatterns = [
    path('', index),
    path('userlist/', UserApiList.as_view(), name='user_list'),
    path('register/', UserRegistrationList.as_view() , name="register"),
    path('api/v1/inn/<str:inn>/', get_inn_user),
    path('api/v1/profiles/', ProfileApiCreate.as_view()),
    path('api/v1/<str:role>/<int:limit>', ProfileApiView.as_view()),
    path('media/img/')
]
