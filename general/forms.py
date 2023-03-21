from django import forms

class BuscarEmpleado(forms.Form):
    area = forms.CharField(max_length=30)
    puesto = forms.CharField(max_length=30)
    dependientes = forms.IntegerField()

class AgregarMedico(forms.Form):
    especialidad = forms.CharField(max_length=30)
    anios_prof = forms.IntegerField()

class AgregarPaciente(forms.Form):
    seguro_medico = forms.CharField(max_length=30)
    estudio = forms.CharField(max_length=30) 