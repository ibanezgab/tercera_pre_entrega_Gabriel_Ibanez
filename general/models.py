from django.db import models

# Create your models here.


class Persona:
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=20)
    correo = models.EmailField()

class Empleado(models.Model,Persona):
    area = models.CharField(max_length=30, default='')
    puesto = models.CharField(max_length=30, default='')
    dependientes = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.id} - {self.area} - {self.puesto} - {self.dependientes}"
    

class Medico(models.Model,Persona):
    especialidad = models.CharField(max_length=30, default='')
    anios_prof = models.IntegerField(default=0) 
    
    def __str__(self):
        return f"{self.id} - {self.especialidad} - {self.anios_prof}"
    
class Paciente(models.Model,Persona):
    seguro_medico = models.CharField(max_length=30,default=0)
    estudio = models.CharField(max_length=30, default='')
    
    def __str__(self):
        return f"{self.id} - {self.estudio}  - {self.seguro_medico}"