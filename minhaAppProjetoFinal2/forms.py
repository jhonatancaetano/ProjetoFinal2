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

class formPostagemCadastroIncidenteInterno(forms.Form):
    #idEvento = forms.IntegerField(primary_key=True)
    data = forms.DateField()
    hora = forms.TimeField()
    local = forms.CharField()
    descricao = forms.CharField()
    #idGerente = forms.ForeignKey("Gerente", on_delete=forms.CASCADE)
    #idUsuario = forms.ForeignKey("Usuario", on_delete=forms.CASCADE)

class formPostagemCadastroLotacao(forms.Form):
    #idLotacao = forms.IntegerField(primary_key=True)
    dia = forms.DateField()
    hora = forms.TimeField()
    faixaHoraria = forms.DateTimeField()
    #idGerente = forms.ForeignKey("Gerente", on_delete=forms.CASCADE)
    #idUsuario = forms.ForeignKey("Usuario", on_delete=forms.CASCADE)
    #idNivel = forms.ForeignKey("NivelDeLotacao", on_delete=forms.CASCADE)
    #idFilial = forms.ForeignKey("Filial", on_delete=forms.CASCADE)

class formPostagemCadastroRecomendacao(forms.Form):
    #idRecomendacao = forms.IntegerField(primary_key=True)
    data = forms.DateField()
    hora = forms.TimeField()
    texto = forms.CharField()
    #idUsuario = forms.ForeignKey("Usuario", on_delete=forms.CASCADE)
    #idFilial = forms.ForeignKey("Filial", on_delete=forms.CASCADE)
    
class formPostagemCadastroIntensDeConsumo(forms.Form):
    #idLotacao = forms.IntegerField(primary_key=True)
    nome = forms.CharField()
    preco = forms.FloatField()
    #idUsuario = forms.ForeignKey("Usuario", on_delete=forms.CASCADE)
    #idClassificacao = forms.ForeignKey("ClassificacaoDoItem", on_delete=forms.CASCADE)
    #idFilial = forms.ForeignKey("Filial", on_delete=forms.CASCADE)
    
class formPostagemCadastroComentario(forms.Form):
    #idComentario = forms.IntegerField(primary_key=True)
    data = forms.DateField()
    hora = forms.TimeField()
    conteudo = forms.CharField()
   