from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from sales import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sales/', include('sales.urls')),
    path('customer/', include('customer.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('common/', include('common.urls')),
    path('', views.index, name='index'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
