from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path

import email_confirmation.views
from Offer import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('offer/', include('offer_start.urls')),
    path('auth/', include('djoser.urls')),
    re_path('auth/', include('djoser.urls.authtoken')),
    path('send/', email_confirmation.views.send)
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
