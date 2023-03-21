from django.shortcuts import render
from  django.http     import HttpResponse
from general.forms import BuscarEmpleado, AgregarMedico, AgregarPaciente
from general.models import Empleado , Paciente, Medico


# Create your views here.

def index(request):
    return render(request,'general/index.html',{"pag":"index"})

def administrativos(request):
    return render(request,'general/administrativos.html',{"pag":"administrativos"})

def medicos(request):
    return render(request,'general/medicos.html',{"pag":"medicos"})

def pacientes(request):
    return render(request,'general/pacientes.html',{"pag":"pacientes"})

def guardar_form(request):

    if request.method == 'POST':

        miFormulario = BuscarEmpleado(request.POST) # Aqui me llega la informacion del html
        print(miFormulario)
        
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            print(f"\n{informacion}\n")
            emp = Empleado(area=informacion["area"],puesto=informacion["puesto"],dependientes=informacion["dependientes"])
            emp.save()
            return render(request, "general/index.html")
    else:
        miFormulario = BuscarEmpleado()
    
    return render(request, "general/guardar_form.html", {"miFormulario": miFormulario})

def guardar_data(request):

    if request.method == 'POST':

        miFormulario = AgregarMedico(request.POST) # Aqui me llega la informacion del html
        print(miFormulario)
        
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            print(f"\n{informacion}\n")
            med = Medico(especialidad=informacion["especialidad"],anios_prof=informacion["anios_prof"])
            med.save()
            return render(request, "general/index.html")
    else:
        miFormulario = AgregarMedico()
    
    return render(request, "general/guardar_data.html", {"miFormulario": miFormulario})

def guardar_info(request):

    if request.method == 'POST':

        miFormulario = AgregarPaciente(request.POST) # Aqui me llega la informacion del html
        print(miFormulario)
        
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            print(f"\n{informacion}\n")
            pas = Paciente(seguro_medico=informacion["seguro_medico"],estudio=informacion["estudio"])
            pas.save()
            return render(request, "general/index.html")
    else:
        miFormulario = AgregarPaciente()
    
    return render(request, "general/guardar_info.html", {"miFormulario": miFormulario})

def buscar_dato_emp(request):

    return render(request,"general/buscar_dato_emp.html")


def buscar(request):

    if request.GET["area"]:

        area = request.GET["area"]
        areas=Empleado.objects.filter(area__icontains=area).values('id','area','puesto','dependientes')

        return render(request,"general/buscar.html",{"areas":areas,"area":area})
    else:
        return render(request,"general/buscar_dato_emp.html")
