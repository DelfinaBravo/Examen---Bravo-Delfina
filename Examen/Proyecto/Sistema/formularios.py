from django import forms
from .models import *

class Nuevo_Producto(forms.ModelForm):
    class Meta: 
        model = Productos
        fields = ['Codigo', 'Nombre', 'Precio', 'Descripcion', 'Imagen']