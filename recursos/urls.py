from django.conf.urls import url
from . import views

urlpatterns = [
	# /recursos/
    url(r'^$', views.index, name='index'),
	# /recursos/login
    url(r'^login/$', views.web_login, name='login'),
	# /recursos/logout
    url(r'^logout/$', views.web_logout, name='logout'),
	# /recursos/usuarios
    url(r'^usuarios/$', views.usuarios, name='usuarios'),
	# /recursos/usuarios/2
	url(r'^usuarios/(?P<id_usuario>\d+)', views.usuario, name='usuario'),
	# /recursos/nuevo
    url(r'^nuevo/$', views.nuevo_recurso, name='nuevo_recurso'),
	# /recursos/3
    url(r'^(?P<id_recurso>\d+)/$', views.recurso, name='recurso'),
	# /recursos/categorias
    url(r'^categorias/$', views.categorias, name='categorias'),
	# /recursos/categorias/4
	url(r'^categoria/(?P<id_categoria>\d+)/$', views.categoria, name='categoria')
]