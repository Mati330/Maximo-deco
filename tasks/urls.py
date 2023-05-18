from django.contrib import admin
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    
    path('', index, name='index'),    
    path('signup/', signup, name='signup'),
    path('signin/', signin, name='signin'),
    path('logout/', signout, name='logout'),  
    path('area_soporte/', area_soporte, name='area_soporte'),    
    path('area_desarrollo/', area_desarrollo, name='area_desarrollo'),
    path('area_swbase/', area_swbase, name='area_swbase'),
    path('area_redes/', area_redes, name='area_redes'),
    path('area_tel/', area_tel, name='area_tel'),
    path('area_seginf/', area_seginf, name='area_seginf'),
    path('formularios/', formularios, name='formularios'),  
    path('capacitacion/', capacitacion, name='capacitacion'),
    path('flow/', flow, name='flow'),
    path('incidentes/', incidentes, name='incidentes'),
    path('referentes/', referentes, name='referentes'),
    path('formulario/', formulario, name='formulario'),
    path('generar_excel/', generar_excel, name='generar_excel'),
    path('error_excel/', error_excel, name='error_excel'),
    path('exito/', exito, name='exito'),
    
    path('ver_errores_soporte/<pk>', ver_errores_soporte.as_view(), name='ver_errores_soporte'),
    path('ver_errores_desarrollo/<pk>', ver_errores_desarrollo.as_view(), name='ver_errores_desarrollo'),
    path('ver_errores_swbase/<pk>', ver_errores_swbase.as_view(), name='ver_errores_swbase'),
    path('ver_errores_redes/<pk>', ver_errores_redes.as_view(), name='ver_errores_redes'),
    path('ver_errores_seginf/<pk>', ver_errores_seginf.as_view(), name='ver_errores_seginf'),
    path('ver_formularios/<pk>', ver_formularios.as_view(), name='ver_formularios'),
    path('ver_capacitacion/<pk>', ver_capacitacion.as_view(), name='ver_capacitacion'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)