from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from recursos.forms import *


def index(request):
	ultimos_rec = Recurso.objects.all().order_by('-id')[:8]
	context = { 'ultimos_rec': ultimos_rec }
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
	

###-------------------Gestión de recursos----------------------------###
# Nuevo recurso
def nuevo_recurso(request):
	if request.method == 'POST':
		nuevo_rec_form = NuevoRecursoForm(request.POST)
		
		if nuevo_rec_form.is_valid():
			#nuevo_rec_form.fecha_pub = 
			nuevo_recurso = nuevo_rec_form.save()

			return redirect('recursos:recurso', nuevo_recurso.id)

		else:   # Formulario no válido
			context = { 'nuevo_rec_form': nuevo_rec_form }

			return render(request, 'recursos/nuevo_recurso.html', context)

	else:
		nuevo_rec_form = NuevoRecursoForm()

		context = { 'nuevo_rec_form': nuevo_rec_form }

		return render(request, 'recursos/nuevo_recurso.html', context)

# Vista recurso
def recurso(request, id_recurso):
	recurso = get_object_or_404(Recurso, pk = id_recurso)
	
	return render(request, 'recursos/recurso.html', { 'recurso': recurso })


###-------------------Gestión de categorias----------------------------###
def categorias(request):
	categorias = Categoria.objects.all()
	
	return render(request, 'recursos/categorias.html', {'categorias': categorias})
	
	
def categoria(request, id_categoria):
	categoria = get_object_or_404(Categoria, pk = id_categoria)
	
	return render(request, 'recursos/categoria.html', {'categoria': categoria})
	
	