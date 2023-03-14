from django.urls import path
from django.conf.urls.static import static
from django.views.static import serve
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('drukarka/',views.home, name='home'),
    path('temp/',views.temp, name='temp'),
    path('upload_file/',views.upload_file, name='upload_file'),
    path('upload/',views.upload, name='upload'),
    path('media/<path:path>', serve, {'document_root': settings.MEDIA_ROOT})
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)