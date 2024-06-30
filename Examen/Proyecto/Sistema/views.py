from django.shortcuts import render, redirect
from .formularios import Nuevo_Producto
from .models import Productos
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.

def Home(request):
    return render(request, "index.html")

def Registrar(request):
    data = {
        'form': Nuevo_Producto()
    }
    if request.method == 'POST':
        registrar = Nuevo_Producto(data=request.POST, files=request.FILES)
        if registrar.is_valid():
            registrar.save()
            data["mensaje"] = "Datos registrados correctamente!"
        else:
            data["form"] = registrar
    return render(request, "Pages/registrar.html", data)

def listar(request):
    listarr = Productos.objects.all() 
    data = {
        'listarr': listarr
    }
    return render(request, "Pages/listar.html", data)

def productos_view(request):  
    data = {
        'form': Nuevo_Producto()
    }
    return render(request, "Pages/productos.html", data)


def salir(request):
    logout(request)
    return redirect("home")