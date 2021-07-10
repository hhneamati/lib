from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework.authtoken.views import obtain_auth_token
from .api_urls import router


urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , include('book.urls')),
    
    path('api-token/', obtain_auth_token),
    path('api/' , include(router.urls)),
    path('api-auth',include('rest_framework.urls'))
]

if settings.DEBUG:
        urlpatterns += static(settings.STATIC_URL,
                              document_root=settings.STATIC_ROOT)
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
