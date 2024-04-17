

from django.contrib import admin
from django.urls import path, include

from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from config import settings

schema_view = get_schema_view(
   openapi.Info(
      title="Qatagon APII",
      default_version='v1',
      description="DRF test",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="No contact here"),
      license=openapi.License(name="No License here"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('qaragon/', include('app_qatagon.urls')),
    path('people/', include('app_people.urls')),
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('accounts/', include('users.urls')),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]