from django.db import models 
from ckeditor.fields import RichTextField

# Create your models here.
class Productos(models.Model):
    Codigo = models.IntegerField(primary_key=True)
    Nombre = models.CharField(max_length=25)
    Precio = models.FloatField()
    Descripcion = RichTextField()
    Imagen = models.ImageField(upload_to="productos", null=True)
    
    def __str__(self):
        return f"{self.Nombre} ({self.Codigo})"

