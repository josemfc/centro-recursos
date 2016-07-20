from django import forms
from django.forms import ModelForm
from django.utils.translation import ugettext as _
from django.utils.html import escape

from recursos.models import *

# Usuarios
class LoginForm (forms.Form):
	name = forms.CharField (label      = 'Nombre de usuario', 
							max_length = 30, 
							required   = False,
							)
	
	passw = forms.CharField ( label = 'Contraseña',
								 max_length = 30,
								 widget = forms.PasswordInput(), 
								 required = False,
	)
	
	def clean(self):
		cleaned_data = super(LoginForm, self).clean()
		n = escape(self.cleaned_data.get('name'))
		p = escape(self.cleaned_data.get('passw'))
		
		if n == '' or p == '':
			raise forms.ValidationError(_('Por favor, introduzca usuario y contraseña para entrar.'))

"""
class NuevoUsuarioForm(forms.Form):
	username = forms.CharField(label  = 'Nombre de usuario', max_length = 30)
	password = forms.CharField (label = 'Contraseña', max_length = 30, widget=forms.PasswordInput())
	email = forms.EmailField(label='Correo electrónico')
	nombre = forms.CharField(label = 'Nombre', max_length = 30, required = False)
	apellidos = forms.CharField(label = 'Apellidos', max_length = 30, required = False)
	es_gestor = forms.BooleanField(label = 'Gestor', required = False)

	def clean(self):
		cleaned_data = super(NuevoUsuarioForm, self).clean()
		
		us = escape(self.cleaned_data.get('username'))
		
		if User.objects.all().filter(username=us).exists():
			raise forms.ValidationError('El usuario \'%s\' ya existe.' % us)


class ModUsuarioForm(forms.Form):
	def __init__(self, usuario, *args, **kwargs):
		super(ModUsuarioForm,self).__init__(*args,**kwargs)
		self.usuario = usuario
		self.min_length = 8
		
		self.fields['nombre'] 		= 	forms.CharField(initial = self.usuario.first_name, required=False)
		self.fields['apellidos'] 	= 	forms.CharField(initial = self.usuario.last_name, required=False)
		self.fields['email'] 		= 	forms.EmailField(initial = self.usuario.email, required=False)
		self.fields['es_gestor'] 	= 	forms.BooleanField(initial = usuario.groups.filter(name='Gestores').exists(), required=False)

	old_pass = forms.CharField (label = 'Contraseña actual', max_length = 30, widget=forms.PasswordInput(), required=False)
	new_pass = forms.CharField (label = 'Nueva contraseña', max_length = 30, widget=forms.PasswordInput(), required=False)
	new_pass2 = forms.CharField (label = 'Repita la nueva contraseña', max_length = 30, widget=forms.PasswordInput(), required=False)

	def clean (self):
		cleaned_data = super(ModUsuarioForm, self).clean()
		co = escape(cleaned_data.get("old_pass"))
		c1 = escape(cleaned_data.get("new_pass"))
		c2 = escape(cleaned_data.get("new_pass2"))
		
		if co != "" and len(c1) < self.min_length:
			raise forms.ValidationError(_('La contraseña debe tener al menos ocho caracteres.'))
		elif co != "" and not self.usuario.check_password(co):
			raise forms.ValidationError(_('Contraseña actual incorrecta.'))
		elif co != "" and co == c1:
			raise forms.ValidationError(_('La contraseña antigua y la nueva no pueden ser iguales.'))
		elif c1 != "" and c1 != c2:
			raise forms.ValidationError(_('Los campos de contraseña nueva no coinciden.'))


class RecuperarForm(forms.Form):
	username = forms.CharField(label  = 'Nombre de usuario', max_length = 30, required = False)
	email = forms.EmailField(label = 'Correo electrónico', required = False)
	
	def clean(self):
		cleaned_data = super(RecuperarForm, self).clean()
		u = escape(self.cleaned_data.get('username'))
		e = escape(self.cleaned_data.get('email'))
		
		if u == '' or e == '':
			raise forms.ValidationError(_('Por favor, rellene ambos campos para continuar.'))
"""

# Video
class NuevoVideoForm (forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(NuevoVideoForm, self).__init__(*args, **kwargs)
		self.fields['titulo'].label = "Título"
		self.fields['titulo'].widget.attrs['size'] = 50
		self.fields['enlace'].widget.attrs['size'] = 50
		self.fields['duracion'].label = "Duración ('HH:MM:SS')"
		self.fields['duracion'].widget = forms.TimeInput(format='%M:%S')
		self.fields['duracion'].required = False
			
	class Meta:
		model = Video
		exclude = ['fecha_pub', 'visualizaciones']
			
		def clean(self):
			cleaned_data = super(NuevoVideoForm, self).clean()
			enl = escape(self.cleaned_data.get('enlace'))
			
			if Video.objects.filter(enlace = enl).exists():
				raise forms.ValidationError(_("Error: El vídeo introducido ya existe en la base de datos."))


class ModVideoForm(forms.ModelForm):
	def __init__(self, vid, *args, **kwargs):
		self.vid = vid
		super(ModVideoForm, self).__init__(*args, **kwargs)
		self.fields['titulo'].initial = vid.titulo
		self.fields['descripcion'].initial = vid.descripcion
		self.fields['duracion'].initial = vid.duracion
		# Categoria

	class Meta:
		model = Video
		fields = ('titulo', 'descripcion', 'duracion')
	
	def save(self, commit=True):
		self.vid.titulo = self.cleaned_data['titulo']
		self.vid.descripcion = self.cleaned_data['descripcion']
		self.vid.duracion = self.cleaned_data['duracion']
		if commit:
			self.vid.save()
		return self.vid

# Foros
"""class NuevoPost (forms.ModelForm):
	class Meta:
		model = Post
		fields = ['content']"""