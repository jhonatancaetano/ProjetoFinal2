from django import forms
from .models import *

"""class formPostagem(forms.Form):
    titulo = forms.CharField()
    texto = forms.CharField()
    data = forms.DateTimeField()
    
class formPostagemCadastroUsuario(forms.Form):
    nomeUsuario = forms.CharField()
    telUsuario = forms.IntegerField()
    emailUsuario  = forms.EmailField()
    senhaUsuario = forms.CharField()
    donoRestautanteUsuario  = forms.BooleanField(required=False)
"""

class formPostagemCadastroEventoExterno(forms.Form):
    dataEvento = forms.DateField()
    horaEvento = forms.TimeField()
    rua = forms.CharField()
    numero = forms.IntegerField()
    bairro = forms.CharField()
    cidade = forms.CharField()
    descricao = forms.CharField()

class formPostagemCadastroIncidenteInterno(forms.ModelForm):
    class Meta:
        model = IncidenteInterno
        fields = ['data', 'hora', 'descricao','idFilial', 'idTipoDeIncidente']

class formPostagemCadastroLotacao(forms.ModelForm):
    class Meta:
        model = Lotacao
        fields = ['dia', 'hora', 'idNivel','idFilial']
        
class formPostagemCadastroItensDeConsumo(forms.ModelForm):
    class Meta:
        model = ItensDeConsumo
        fields = ['idFilial','nomeItem', 'precoItem', 'idClassificacao']

class formPostagemCadastroRecomendacao(forms.ModelForm):
    class Meta:
        model = Recomendacao
        fields = ['idFilial','data', 'hora', 'texto', 'idUsuario']
    
class formPostagemCadastroComentario(forms.ModelForm):
     class Meta:
        model = Comentario
        fields = ['data', 'hora', 'Item','conteudo']
        
class formPostagemCadastroAssociacaoUsuarioUsuario(forms.ModelForm):
     class Meta:
        model = AssociacaoUsuarioUsuario
        fields = ['idUsuarioSecundario', 'idTipoRelacionamento']