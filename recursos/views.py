from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from recursos.forms import *


def index(request):
	ultimos_vid = Video.objects.all().order_by('-id')[:8]
	context = { 'ultimos_vid': ultimos_vid }
	return render(request, 'recursos/index.html', context)
	

###-------------------Gestión de usuarios----------------------------###
# Formulario de login
def web_login(request):
 
	if request.method == 'GET':
		form = LoginForm()
		context = {
			'form': form,
		}
 
		return render(request, 'recursos/login.html', context)
 
	else:
		form = LoginForm (request.POST)
 
		if form.is_valid ():
			usuario = escape(form.cleaned_data['name'])
			contrasenia = escape(form.cleaned_data['passw'])
 
			user = authenticate(username = usuario, password = contrasenia) # Verificar usuario y contraseña
 
			if user is not None and user.is_active:
				login (request, user)   # Éxito
 
				return redirect('recursos:index')
 
			else:
				context = {
					'mensaje':'* Usuario y contraseña no válidos.',
					'form': form,
				}
				return render (request, 'recursos/login.html', context)
         
		else:   # Formulario no válido (campo vacío)
			context = {
				'form': form,
			}
			return render (request, 'recursos/login.html', context)


# Desconectarse de la página 
@login_required
def web_logout(request):
    logout(request)
    return redirect('recursos:index')
	
	
# Listado de usuarios
@login_required
def usuarios(request):
	lista_usuarios = User.objects.filter().order_by('username')
	paginator = Paginator(lista_usuarios, 10) # 10 usuarios por página

	page = request.GET.get('page')
	try:
		usuarios = paginator.page(page)
	except PageNotAnInteger:		# If page is not an integer, deliver first page.
		usuarios = paginator.page(1)
	except EmptyPage:				# If page is out of range (e.g. 9999), deliver last page of results.
		usuarios = paginator.page(paginator.num_pages)
	
	context = {
		'usuarios': usuarios,
	}

	return render(request, 'recursos/usuarios.html', context)
	
	
# Mostrar usuario
@login_required
def usuario(request, id_usuario):
	usuario = get_object_or_404(User, pk=id_usuario)

	return render(request, 'recursos/usuario.html', { 'usuario': usuario })
	

###-------------------Gestión de vídeos----------------------------###
# Nuevo vídeo
@login_required
@permission_required("auth.es_gestor", login_url="recursos:index")
def nuevo_video(request):
	if request.method == 'POST':
		nuevo_vid_form = NuevoVideoForm(request.POST)
		
		if nuevo_vid_form.is_valid():
			#nuevo_vid_form.fecha_pub = 
			nuevo_video = nuevo_vid_form.save()

			return redirect('recursos:video', nuevo_video.id)

		else:   # Formulario no válido
			context = { 'nuevo_vid_form': nuevo_vid_form }

			return render(request, 'recursos/nuevo_video.html', context)

	else:
		nuevo_vid_form = NuevoVideoForm()

		context = { 'nuevo_vid_form': nuevo_vid_form }

		return render(request, 'recursos/nuevo_video.html', context)

# Vista vídeo
def video(request, id_video):
	video = get_object_or_404(Video, pk = id_video)
	
	return render(request, 'recursos/video.html', { 'video': video })

# Modificar un vídeo
@login_required
@permission_required('auth.es_gestor', login_url="recursos:index")
def mod_video(request, id_video):
	video = get_object_or_404(Video, pk=id_video)
	
	if request.method == 'POST':
		modform = ModVideoForm(video, request.POST)

		if modform.is_valid():
			mod_video = modform.save()

			return redirect('recursos:video', mod_video.id)

		else:   # Formulario no válido
			context = {'video': video, 'modform': modform }

			return render(request, 'recursos/mod_video.html', context)
	else:	# GET
		modform = ModVideoForm(video)
		context = { 
			'video': video,
			'modform': modform
		}

		return render(request, 'recursos/mod_video.html', context)


# Borrar vídeo
@login_required
@permission_required('auth.es_gestor', login_url="recursos:index")
def borrar_video(request, id_video):
	video = get_object_or_404(Video, pk=id_video).delete()
	return redirect('recursos:videos')


###-------------------Gestión de categorias----------------------------###
def categorias(request):
	categorias = Categoria.objects.all()
	
	return render(request, 'recursos/categorias.html', {'categorias': categorias})
	
	
def categoria(request, id_categoria):
	categoria = get_object_or_404(Categoria, pk = id_categoria)
	
	return render(request, 'recursos/categoria.html', {'categoria': categoria})
	

###-------------------Gestión de foros----------------------------###
"""def foros(request):
	categorias = Categoria.objects.all()
	
	return render(request, 'recursos/foros.html', {'categorias': categorias})

def cat_foros(request, id_categoria):
	categoria = get_object_or_404(Categoria, pk = id_categoria)
	foros = Foro.objects.filter(categoria = categoria)

	return render(request, 'recursos/categorias_foros.html', { 'foros': foros })

def foro(request, id_foro):
	foro = get_object_or_404(Foro, pk = id_foro)
	posts = Post.objects.filter(foro = foro)
	
	if request.method == 'POST':
		post_form = NuevoRecursoForm(request.POST)
	else:
		post_form = NuevoRecursoForm()
	
	context = {
		'foro': foro,
		'posts': posts,
		#'post_form': nuevo_rec_form,
	}
	
	return render(request, 'recursos/foro.html', context)"""

