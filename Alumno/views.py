from django.shortcuts import render,redirect
from .form import AlumnosModelForm
from .models import Alumnos
from django.db.models import Q

# Create your views here.
def Inicio(request):
    
    if request.method == 'POST':
        query = request.POST['query']
        objs = Alumnos.objects.filter(
            Q(Nombre__contains=query)|
            Q(Apellido__contains=query)|
            Q(Correo__contains=query)|
            Q(Telefono__contains=query))
    else:
        objs = Alumnos.objects.all()
        
    contex = {
        "Alumnos":objs,
    }
    return render(request,'Inicio.html',context=contex)

def Agregar(request):
    form = AlumnosModelForm
    context={
        'formulario':form,
        }
    if request.method == 'POST':
        formulario = form(data=request.POST ,files=request.FILES) 
        if formulario.is_valid():
            formulario.save()
            return redirect('inicio') 
  
    return render(request,'agregar.html',context=context)

def Editar(request,id):
    alum = Alumnos.objects.get(pk=id)
    form = AlumnosModelForm(instance=alum)
    
    if request.method == 'POST':
        form = AlumnosModelForm(request.POST ,request.FILES,instance=alum) 
        if form.is_valid():
            form.save()
            return redirect('inicio') 
    context={
        'alumno':alum,
        'formulario':form,
        }
    return render(request,'editar.html',context=context)

def Borrar(request,id):

   Alumnos.objects.get(id=id).delete()
   
   return redirect('inicio')

def Detalles(request,id):
    detalle = Alumnos.objects.get(id=id)
    return render(request,'detalles.html',context={
        'detalle':detalle
    })
