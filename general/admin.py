from django.contrib import admin
from general.models import Empleado, Medico , Paciente

# Register your models here.

admin.site.register(Empleado)

admin.site.register(Medico)

admin.site.register(Paciente)
