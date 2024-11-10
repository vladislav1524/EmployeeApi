from django.contrib import admin
from django.urls import path, re_path, include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.authtoken import views


# схема доментации API
schema_view = get_schema_view(
    openapi.Info(
        title="API",
        default_version='v1',
        description="Api для работы с данными по сотрудникам и департаментам",
        contact=openapi.Contact(email="contact@yourapi.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    re_path(r'^$', RedirectView.as_view(url='/api/', permanent=True)), # Перенаправление с главной страницы
    path('api/', include('api.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', views.obtain_auth_token), # получение токена аутентификации
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
