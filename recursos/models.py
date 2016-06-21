from django.db import models


class Categoria(models.Model):
	nombre = models.CharField(max_length=50)
	
	def __str__(self):
		return self.nombre

class Recurso(models.Model):
	titulo = models.CharField(max_length=200)
	descripcion = models.TextField(max_length=500)
	enlace = models.URLField(unique = True)
	fecha_pub = models.DateTimeField('fecha publicacion', auto_now_add=True)
	duracion = models.TimeField(default= "00:00")
	visualizaciones = models.IntegerField(default = 0)
	categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
	
	TIPOS_RECURSOS = ( (0,'pdf'), (1,'video'))
	tipo = models.IntegerField(default=0, choices=TIPOS_RECURSOS)
	
	def __str__(self):
		return self.titulo
