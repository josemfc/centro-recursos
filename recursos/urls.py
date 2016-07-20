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
	url(r'^usuarios/(?P<id_usuario>\d+)/', views.usuario, name='usuario'),
	# /recursos/nuevo
	url(r'^nuevo/$', views.nuevo_video, name='nuevo_video'),
	# /recursos/3
	url(r'^(?P<id_video>\d+)/$', views.video, name='video'),
	# /recursos/3/mod
	url(r'^(?P<id_video>\d+)/mod/$', views.mod_video, name='mod_video'),
	# /recursos/3/borrar
	url(r'^(?P<id_video>\d+)/borrar/$', views.borrar_video, name='borrar_video'),
	# /recursos/categorias
	url(r'^categorias/$', views.categorias, name='categorias'),
	# /recursos/categorias/4
	url(r'^categoria/(?P<id_categoria>\d+)/$', views.categoria, name='categoria'),
]

"""# /recursos/foros
url(r'^foros/$', views.foros, name='foros'),
# /recursos/foros/categoria/4
url(r'^foros/categoria/(?P<id_categoria>\d+)/$', views.cat_foros, name='cat_foros'),
# /recursos/foros/5
url(r'^foros/(?P<id_foro>\d+)/$', views.foro, name='foro'),"""