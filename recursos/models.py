from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User, Group, Permission


class Categoria(models.Model):
	nombre = models.CharField(max_length=50)
	
	def __str__(self):
		return self.nombre

class Video(models.Model):
	titulo = models.CharField(max_length=200)
	descripcion = models.TextField(max_length=500)
	enlace = models.URLField(unique = True)
	fecha_pub = models.DateTimeField('fecha publicacion', auto_now_add=True)
	duracion = models.TimeField()
	visualizaciones = models.IntegerField(default = 0)
	categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
	
	def __str__(self):
		return self.titulo


class Comentario(models.Model):
	video = models.ForeignKey(Video, on_delete=models.CASCADE)
	usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
	respuestas = models.ForeignKey('self', on_delete=models.CASCADE)
	contenido = RichTextField()
	fecha_escrito = models.DateTimeField('escrito el día', auto_now_add=True)

	def __str__(self):
		return "Comentario de " + self.usuario.username + " en " + self.video.titulo


class Tag(models.Model):
	etiqueta = models.CharField(max_length = 30)


class Tagvid(models.Model):
	tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
	video = models.ForeignKey(Video, on_delete=models.CASCADE)

"""class Foro(models.Model):
	categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
	titulo = models.CharField(max_length = 100)
	
	def __str__(self):
		return self.titulo
"""