""" docstring """
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from django.conf.urls.static import static


schema_view = get_schema_view(
   openapi.Info(
      title="TODAY WORKOUT DONE API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="Test License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
   path('admin/', admin.site.urls),
   path('articles/', include('articles.urls')),
   path('users/', include('users.urls')),
   path('social_auth/', include(('social_auth.urls', 'social_auth'), namespace="social_auth")),
   path('challenges/', include('challenges.urls')),
   path('achievements/', include('achievements.urls')),
########################################################################################
   # path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   # path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
handler404='utils.views.error_404'
handler500='utils.views.error_500'
