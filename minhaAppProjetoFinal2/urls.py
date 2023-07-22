from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from . import views


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
	url(r'^excluirIncidente/', views.excluirIncidente, name="excluirIncidente"),
	url(r'^burrito/', views.burrito, name="burrito"),
	url(r'^get_itens_by_filial/', views.get_itens_by_filial, name='get_itens_by_filial'),
]