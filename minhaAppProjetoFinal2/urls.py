from django.conf.urls import url, include
from django.contrib import admin
from . import views
from django.urls import path

urlpatterns = [

	url(r'^login/', views.login, name="login"),
	url(r'^cadastro/', views.cadastro, name="cadastro"),
	url(r'^perfil/', views.perfil, name="perfil"),
	url(r'^meusrestaurantes/', views.meusrestaurantes, name="meusrestaurantes"),
	url(r'^cadastroeventoexterno/', views.cadastroeventoexterno, name="cadastroeventoexterno"),
	url(r'^buscarusuarios/', views.buscarusuarios, name="buscarusuarios"),
	url(r'^inserePostagem/', views.inserePostagem, name="inserePostagem"),
	url(r'^cadastroincidenteinterno/', views.cadastroincidenteinterno, name="cadastroincidenteinterno"),
	url(r'^lotacao/', views.lotacao, name="lotacao"),
	url(r'^comentarios/', views.comentarios, name="comentarios"),
	url(r'^recomendacao/', views.recomendacao, name="recomendacao"),
	url(r'^exibirEventoExterno/', views.exibirEventoExterno, name="exibirEventoExterno"),
	url(r'^exibirincidenteinterno/', views.exibirincidenteinterno, name="exibirincidenteinterno"),
	url(r'^exibirlotacao/', views.exibirlotacao, name="exibirlotacao"),
	url(r'^exibirRecomendacao/', views.exibirRecomendacao, name="exibirRecomendacao"),
	url(r'^exibirComentario/', views.exibirComentario, name="exibirComentario"),
	url(r'^itensDeConsumo/', views.itensDeConsumo, name="itensDeConsumo"),
    url(r'^exibirItens/', views.exibirItens, name='exibirItens'),
	url(r'^editarincidenteinterno/', views.editarincidenteinterno, name="editarincidenteinterno"),
	url(r'^associacaoUsuarios/', views.associacaoUsuarios, name="associacaoUsuarios"),
]