
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path

from Offer import settings
from clean.views import *

urlpatterns = [
     path('', EditProductPrice.as_view()),
     path('product/my/', MyProductsApi.as_view()),
     path('product/my/<int:pk>/',EditMyProduct.as_view()),
     path('product/all/', AllProductApi.as_view()),
     path('product/id<int:id>/', GetUserProduct.as_view())



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

