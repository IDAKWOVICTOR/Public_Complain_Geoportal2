from django.urls import path
from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


admin.site.site_header = "PUBLIC COMPLAINS GEOPORTAL"


urlpatterns = [
    path('', views.index, name='index'),
    path('submit/', views.submit_complaint, name='submit_complaint'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


