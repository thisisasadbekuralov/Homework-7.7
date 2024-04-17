from django.urls import path
from rest_framework import routers

from .views import AffectedIndividualsViewSet

router = routers.DefaultRouter()
router.register(r'', AffectedIndividualsViewSet, basename='people')

urlpatterns = router.urls