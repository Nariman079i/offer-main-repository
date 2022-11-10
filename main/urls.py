from django.conf.urls.static import static
from django.urls import path, include, re_path
from Offer.settings import *
from main.views import *

urlpatterns = [
    path('', index),
    #path('userlist/', UserApiList.as_view(), name='user_list'),
    #path('register/', UserRegistrationList.as_view() , name="register"),
    #path('api/v1/inn/<str:inn>/', get_inn_user),
    path('api/v1/profiles/', ProfileApiCreate.as_view()),
    path('api/v1/<str:role>/', ProfileApiList.as_view()),
    path('api/v1/<str:role>/<int:limit>/', ProfileApiView.as_view()),
    path('auth/', include('djoser.urls')),
    re_path('auth/', include('djoser.urls.authtoken'))

]+ static(MEDIA_URL, document_root=MEDIA_ROOT)

