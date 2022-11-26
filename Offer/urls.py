
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path

from Offer import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('offer/', include('offer_start.urls')),
    path('auth/', include('djoser.urls')),
    re_path('auth/', include('djoser.urls.authtoken'))
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

