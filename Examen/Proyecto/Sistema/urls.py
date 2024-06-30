from django.urls import path
from .views import *

urlpatterns = [
    path('',Home, name="home"),
    path('registrar/', Registrar, name = "registrar"),
    path('salir/', salir, name = "salir"),
    path('listar/', listar, name = "listar"),
    path('productos/', Productos, name = "productos"),
      
]
