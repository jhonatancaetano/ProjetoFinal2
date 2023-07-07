from django import forms

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
    #idEvento = forms.IntegerField(primary_key=True)
    dataEvento = forms.DateField()
    horaEvento = forms.TimeField()
    rua = forms.CharField()
    numero = forms.IntegerField()
    bairro = forms.CharField()
    cidade = forms.CharField()
    descricao = forms.CharField()
    #idGerente = forms.ForeignKey("Gerente", on_delete=forms.CASCADE)
    #idUsuario = forms.ForeignKey("Usuario", on_delete=forms.CASCADE)
