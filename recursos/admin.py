from django.contrib import admin
from django.contrib.auth.models import Permission

from .models import *

admin.site.register(Permission)
admin.site.register(Categoria)
admin.site.register(Video)
admin.site.register(Comentario)
admin.site.register(Tag)
admin.site.register(Tagvid)