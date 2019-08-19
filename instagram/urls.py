from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static #static 로드할 떄 꼭 필요
from django.conf import settings # settings 로드할 떄 필요

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('insta.urls')),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)