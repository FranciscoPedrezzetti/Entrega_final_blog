from django.db import models
from django.contrib.auth.models import User

# Create your models here.

"""La entrada de texto para cada experiencia de lavado"""
class Post(models.Model):

    name = models.CharField(max_length=60)
    city = models.CharField(max_length=60)
    title = models.CharField(max_length=60, unique=True)
    subtitle = models.CharField(max_length=60)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='post_images/', null=True, blank=True)

class Meta:
     # Nombres a mostrar en singular y plural (admin panel)
     verbose_name = 'entrada'
     verbose_name_plural = "entradas"

     def __str__(self):
       return f"{self.name} - {self.title} - {self.subtitle}"


    ##class Promo(models.Model):
      ##  """Promociones/descuentos en vuelos/actividades, etc."""

    ##categoria = models.CharField(max_length=50)
    ##descripcion = models.CharField(max_length=120)
    ##detalle = models.CharField(max_length=120)
    ##valid_through = models.DateField()

    ##def __str__(self):
      ##  return f"{self.categoria} | {self.descripcion}"

