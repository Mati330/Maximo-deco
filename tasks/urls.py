from django.contrib import admin
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    
    path('', home, name='index'),    
    path('signup', signup, name='signup'),
    path('signin', signin, name='signin'),
    path('logout', signout, name='logout'),  
    path('area_soporte/', area_soporte, name='area_soporte'),    
    path('area_desarrollo/', area_desarrollo, name='area_desarrollo'),
    path('area_swbase/', area_swbase, name='area_swbase'),
    path('area_redes/', area_redes, name='area_redes'),
    path('area_tel/', area_tel, name='area_tel'),
    path('area_seginf/', area_seginf, name='area_seginf'),
    
    path('ver_errores_soporte/<pk>', ver_errores_soporte.as_view(), name='ver_errores_soporte'),
    path('ver_errores_desarrollo/<pk>', ver_errores_desarrollo.as_view(), name='ver_errores_desarrollo'),
    path('ver_errores_swbase/<pk>', ver_errores_swbase.as_view(), name='ver_errores_swbase'),
    path('ver_errores_redes/<pk>', ver_errores_redes.as_view(), name='ver_errores_redes'),
    path('ver_errores_seginf/<pk>', ver_errores_seginf.as_view(), name='ver_errores_seginf'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)