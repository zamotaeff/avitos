from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from ads.views import index_route
from ads.views.ad import AdViewSet
from ads.views.selection import SelectionViewSet
from avito import settings
from users.views import LocationViewSet


router = routers.SimpleRouter()
router.register('location', LocationViewSet)
router.register('ad', AdViewSet)
router.register('selection', SelectionViewSet)

urlpatterns = [
    path('', index_route),

    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),

    path('ad/', include('ads.urls.ad')),
    path('cat/', include('ads.urls.cat')),

    path('user/', include('users.urls'))
]

urlpatterns += router.urls

# To display images when debugging mode
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
