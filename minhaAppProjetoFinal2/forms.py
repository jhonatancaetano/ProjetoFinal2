from django import forms
from .models import Usuario
from .models import Filial
from .models import EventoExterno
from .models import IncidenteInterno
from .models import Lotacao
from .models import ItensDeConsumo
from .models import Comentario
from .models import Recomendacao
from .models import AssociacaoUsuarioUsuario
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse


class formPostagemCadastroEventoExterno(forms.ModelForm):
    class Meta:
        model = EventoExterno
        fields = ['dataEvento', 'horaEvento', 'rua', 'numero', 'bairro', 'cidade', 'descricao']

class formPostagemCadastroIncidenteInterno(forms.ModelForm):
    class Meta:
        model = IncidenteInterno
        fields = ['data', 'hora', 'descricao', 'nomeFilial', 'nomeTipoDeIncidente']

class formPostagemCadastroLotacao(forms.ModelForm):
    class Meta:
        model = Lotacao
        fields = ['dia', 'hora', 'nomeNivel', 'nomeFilial']

class formPostagemCadastroItensDeConsumo(forms.ModelForm):
    class Meta:
        model = ItensDeConsumo
        fields = ['nomeFilial', 'nomeItem', 'precoItem', 'nomeClassificacao']

class formPostagemCadastroRecomendacao(forms.ModelForm):
    class Meta:
        model = Recomendacao
        fields = ['nomeFilial', 'data', 'hora', 'texto']

class formPostagemCadastroComentario(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['nomeFilial', 'nomeItem', 'data', 'hora', 'conteudo']

    def __init__(self, *args, **kwargs):
        filial_queryset = kwargs.pop('filial_queryset', None)
        super(formPostagemCadastroComentario, self).__init__(*args, **kwargs)

        if filial_queryset is not None:
            self.fields['nomeFilial'].queryset = filial_queryset

        self.fields['nomeItem'].queryset = ItensDeConsumo.objects.none()

class formPostagemCadastroAssociacaoUsuarioUsuario(forms.ModelForm):
    class Meta:
        model = AssociacaoUsuarioUsuario
        #fields = ['nomeUsuarioSecundario', 'nomeTipoRelacionamento']
        exclude = ['nomeUsuarioPrincipal']