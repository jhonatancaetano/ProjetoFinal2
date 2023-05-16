from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [

	url(r'^login/', views.login, name="login"),
	url(r'^cadastro/', views.cadastro, name="cadastro"),
	url(r'^perfil/', views.perfil, name="perfil"),
]