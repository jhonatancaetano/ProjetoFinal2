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
	url(r'^cadastroincidenteinterno/', views.cadastroincidenteinterno, name="cadastroincidenteinterno"),
	url(r'^lotacao/', views.lotacao, name="lotacao"),
	url(r'^comentarios/', views.comentarios, name="comentarios"),
	url(r'^recomendacao/', views.recomendacao, name="recomendacao"),
	url(r'^itensDeConsumo/', views.itensDeConsumo, name="itensDeConsumo"),
    url(r'^exibirItens/', views.exibirItens, name='exibirItens'),
	url(r'^associacaoUsuarios/', views.associacaoUsuarios, name="associacaoUsuarios"),
	url(r'^burrito/', views.burrito, name="burrito"),
	url(r'^get_itens_by_filial/', views.get_itens_by_filial, name='get_itens_by_filial'),
]