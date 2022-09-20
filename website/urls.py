 
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users import views
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()

router.register('vendor',views.Vendor_data, basename='vendor_data')
router.register('consumer',views.Consumer_data,basename='consumer_data')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
