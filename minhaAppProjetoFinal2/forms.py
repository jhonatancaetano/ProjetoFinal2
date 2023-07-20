from django import forms
from .models import EventoExterno
from .models import IncidenteInterno
from .models import Lotacao
from .models import ItensDeConsumo
from .models import Comentario
from .models import Recomendacao
from .models import AssociacaoUsuarioUsuario

class formPostagemCadastroEventoExterno(forms.ModelForm):
    class Meta:
        model = EventoExterno
        fields = ['dataEvento', 'horaEvento', 'rua', 'numero', 'bairro', 'cidade', 'descricao', 'nomeUsuario']

    def __init__(self, *args, **kwargs):
        super(formPostagemCadastroEventoExterno, self).__init__(*args, **kwargs)
        self.fields['nomeUsuario'].widget = forms.HiddenInput()

class formPostagemCadastroIncidenteInterno(forms.ModelForm):
    class Meta:
        model = IncidenteInterno
        fields = ['data', 'hora', 'descricao', 'nomeFilial', 'nomeTipoDeIncidente', 'nomeUsuario']

    def __init__(self, *args, **kwargs):
        super(formPostagemCadastroIncidenteInterno, self).__init__(*args, **kwargs)
        self.fields['nomeUsuario'].widget = forms.HiddenInput()

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
        fields = ['nomeFilial', 'data', 'hora', 'texto', 'nomeUsuario']

class formPostagemCadastroComentario(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['data', 'hora', 'nomeItem', 'conteudo']

class formPostagemCadastroAssociacaoUsuarioUsuario(forms.ModelForm):
    class Meta:
        model = AssociacaoUsuarioUsuario
        fields = ['nomeUsuarioSecundario', 'nomeTipoRelacionamento']