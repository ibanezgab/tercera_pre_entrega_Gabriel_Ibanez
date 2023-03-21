#from django.contrib import admin
from django.urls import path
from general.views import *

urlpatterns = [
    #path("admin/", admin.site.urls),
    path('', index, name ='index'),
    path('administrativos/', administrativos, name ='administrativos'),
    path('medicos/', medicos, name ='medicos'),
    path('pacientes/', pacientes, name ='pacientes'),
    path('guardar_form/', guardar_form, name ='guardar_form'),
    path('guardar_data/', guardar_data, name ='guardar_data'),
    path('guardar_info/', guardar_info, name ='guardar_info'),
    path('buscar/', buscar, name ='buscar'),
    path('buscar_dato_emp/', buscar_dato_emp, name ='buscar_dato_emp'),

]
