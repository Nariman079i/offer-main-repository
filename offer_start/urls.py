from rest_framework.routers import DefaultRouter
from django.conf.urls.static import static
from django.urls import path,include
from Offer import settings
from offer_start.views import *

router = DefaultRouter()
router.register(r'investor', CreateInvestor)
router.register(r'businessman', CreateBusinessman)
router.register(r'company', CreateCompany)

urlpatterns = [
    path('create/', include(router.urls))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
