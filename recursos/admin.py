from django.contrib import admin
from django.contrib.auth.models import Permission

from .models import Categoria, Recurso

admin.site.register(Categoria)
admin.site.register(Recurso)
admin.site.register(Permission)