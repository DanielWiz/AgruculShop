from django.db import models

class Producto(models.Model):
	codigo_producto = models.AutoField(primary_key=True)
	nombre = models.CharField(max_length=60)
	descripcion = models.CharField(max_length=120)
	precio = models.IntegerField(default=0)
	imagen_producto = models.ImageField(upload_to = 'img_productos/', default='img_productos/noimage.jpeg')
	stock = models.IntegerField(default=0)
	def __str__(self):
		return "%s. %s" % (self.codigo_producto, self.nombre)
# Create your models here.
