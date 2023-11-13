from django.contrib import admin
from django.urls import path, re_path, include
from .yasg import urlpatterns as doc_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include([
        path('musicstore/', include('instruments.urls')),
    ])),
]
urlpatterns += doc_urls