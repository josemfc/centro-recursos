from django.conf.urls import include, url
from django.contrib import admin

from recursos import views

urlpatterns = [
	url(r'^$', views.index),
    url(r'^recursos/', include('recursos.urls', namespace='recursos')),
    url(r'^admin/', admin.site.urls),
]
