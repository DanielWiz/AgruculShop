from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	Rut = models.CharField(max_length=10)
	Nombre = models.CharField(max_length=500, blank=True)
	Apellido = models.CharField(max_length=30, blank=True)
	Fecha_Nacimiento = models.DateField(null=True, blank=True)


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


class Producto(models.Model):
	Usuario = models.ForeignKey(User, on_delete=models.CASCADE)
	codigo_producto = models.AutoField(primary_key=True)
	nombre = models.CharField(max_length=60)
	descripcion = models.CharField(max_length=120)
	precio = models.IntegerField(default=0)
	imagen_producto = models.ImageField(default='img_productos/ejemplo.jpg', blank = True)
	stock = models.IntegerField(default=0)
	def __str__(self):
		return "%s. %s" % (self.codigo_producto, self.nombre)