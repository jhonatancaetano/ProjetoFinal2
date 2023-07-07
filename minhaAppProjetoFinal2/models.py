from django.db import models

# Create your models here.


"""class postagemcaduser(models.Model):
    idUsuario = models.AutoField(primary_key=True)
    nomeUsuario = models.TextField()
    telUsuario = models.IntegerField()
    emailUsuario  = models.EmailField(max_length=254)
    senhaUsuario = models.TextField()
    donoRestautanteUsuario  = models.BooleanField()
    #titulo = models.CharField(max_length=100)
    #texto = models.TextField()
    #data = models.DateTimeField()
    def __str__(self):
        return self.idUsuario


class postagem(models.Model):
    titulo = models.CharField(max_length=100)
    texto = models.TextField()
    data = models.DateTimeField()
    def __str__(self):
        return self.titulo


class cadastroUsuario(models.Model):
    idUsuario = models.AutoField(primary_key=True)
    nomeUsuario = models.TextField()
    telUsuario = models.IntegerField()
    emailUsuario  = models.EmailField(max_length=254)
    senhaUsuario = models.TextField()
    donoRestautanteUsuario  = models.BooleanField()
    def __str__(self):
        return self.titulo
"""

class TipoDeComida(models.Model):
    idComida = models.AutoField(primary_key=True)
    descComida = models.TextField()
    def __str__(self):
        return self.idComida

class Restaurante(models.Model):
    idRestaurante = models.AutoField(primary_key=True)
    nome = models.TextField()
    idComida = models.ForeignKey("TipoDeComida", on_delete=models.CASCADE)
    def __str__(self):
        return self.idRestaurante

class Filial(models.Model):
    idFilial = models.AutoField(primary_key=True)
    localizacaoGPS = models.TextField()
    rua = models.TextField()
    numero = models.IntegerField()
    def __str__(self):
        return self.idFilial

class Gerente(models.Model):
    idGerente = models.AutoField(primary_key=True)
    def __str__(self):
        return self.idGerente

class RevisaoDeComentario(models.Model):
    idRevisao = models.AutoField(primary_key=True)
    data = models.DateField()
    hora = models.TimeField()
    conteudo = models.TextField()
    def __str__(self):
        return self.idRevisao

class Comentario(models.Model):
    idComentario = models.AutoField(primary_key=True)
    data = models.DateField()
    hora = models.TimeField()
    conteudo = models.TextField()
    def __str__(self):
        return self.idComentario

class ClassificacaoDoItem(models.Model):
    idClassificacao = models.AutoField(primary_key=True)
    descItem = models.TextField()
    def __str__(self):
        return self.idClassificacao

class ItensDeConsumo(models.Model):
    idItem = models.AutoField(primary_key=True)
    nomeItem = models.TextField()
    precoItem = models.FloatField()
    idFilial = models.ForeignKey("Filial", on_delete=models.CASCADE)
    idClassificacao = models.ForeignKey("ClassificacaoDoItem", on_delete=models.CASCADE)
    def __str__(self):
        return self.idItem

class TipoDeRelacionamento(models.Model):
    idRelacionamento = models.AutoField(primary_key=True)
    descTipoRelacionamento = models.TextField()
    def __str__(self):
        return self.idRelacionamento

class Usuario(models.Model):
    idUsuario = models.AutoField(primary_key=True)
    nome = models.TextField()
    numeroTelefone = models.IntegerField()
    email = models.EmailField(max_length=254)
    senha = models.TextField()
    cpf = models.IntegerField()
    idRelacionamento = models.ForeignKey("Relacionamento", on_delete=models.CASCADE)
    def __str__(self):
        return self.idUsuario

class Relacionamento(models.Model):
    #idUsuario1 = models.AutoField(primary_key=True)
    #idUsuario2 = models.AutoField(primary_key=True)
    idUsuario1 = models.ForeignKey("Usuario", on_delete=models.CASCADE)
    #idUsuario2 = models.ForeignKey("Usuario", on_delete=models.CASCADE)
    idTipoRelacionamento = models.ForeignKey("TipoDeRelacionamento", on_delete=models.CASCADE)
    def __str__(self):
        return self.XXX

class NivelDeLotacao(models.Model):
    idNivel = models.AutoField(primary_key=True)
    descNivel = models.TextField()
    def __str__(self):
        return self.idNivel

class Lotacao(models.Model):
    idLotacao = models.AutoField(primary_key=True)
    hora = models.TimeField()
    dia = models.DateTimeField()
    faixaHoraria = models.DateTimeField()
    idUsuario = models.ForeignKey("Usuario", on_delete=models.CASCADE)
    idNivel = models.ForeignKey("NivelDeLotacao", on_delete=models.CASCADE)
    idGerente = models.ForeignKey("Gerente", on_delete=models.CASCADE)
    idFilial = models.ForeignKey("Filial", on_delete=models.CASCADE)
    def __str__(self):
        return self.idLotacao

class TipoDeIncidenteInterno(models.Model):
    idTipoIncidente = models.AutoField(primary_key=True)
    descIncidente = models.TextField()
    def __str__(self):
        return self.idTipoIncidente

class IncidenteInterno(models.Model):
    idIncidente = models.AutoField(primary_key=True)
    descricao = models.TextField()
    data = models.DateField()
    hora = models.TimeField()
    local = models.TextField()
    idFilial = models.ForeignKey("Filial", on_delete=models.CASCADE)
    idTipoIncidente = models.ForeignKey("TipoDeIncidenteInterno", on_delete=models.CASCADE)
    idGerente = models.ForeignKey("Gerente", on_delete=models.CASCADE)
    idUsuario = models.ForeignKey("Usuario", on_delete=models.CASCADE)
    def __str__(self):
        return self.idIncidente

class EventoExterno(models.Model):
    idEvento = models.AutoField(primary_key=True)
    dataEvento = models.DateField()
    horaEvento = models.TimeField()
    rua = models.TextField()
    numero = models.IntegerField()
    bairro = models.TextField()
    cidade = models.TextField()
    descricao = models.TextField()
    #idGerente = models.ForeignKey("Gerente", on_delete=models.CASCADE)
    #idUsuario = models.ForeignKey("Usuario", on_delete=models.CASCADE)
    def __str__(self):
        return self.idEvento

class Recomendacao(models.Model):
    idRecomendacao = models.AutoField(primary_key=True)
    texto = models.TextField()
    data = models.DateField()
    hora = models.TimeField()
    idFilial = models.ForeignKey("Filial", on_delete=models.CASCADE)
    idUsuario = models.ForeignKey("Usuario", on_delete=models.CASCADE)
    def __str__(self):
        return self.idRecomendacao

class AssociacaoFilialEventoExterno(models.Model):
    idFilial = models.ForeignKey("Filial", on_delete=models.CASCADE)
    idEvento = models.ForeignKey("EventoExterno", on_delete=models.CASCADE)

class AssociacaoItemDeConsumoRecomendacao(models.Model):
    idRecomendacao = models.ForeignKey("Recomendacao", on_delete=models.CASCADE)
    idItem = models.ForeignKey("ItensDeConsumo", on_delete=models.CASCADE)

class AssociacaoRestauranteUsuario(models.Model):
    idRestaurante = models.ForeignKey("Restaurante", on_delete=models.CASCADE)
    idUsuario = models.ForeignKey("Usuario", on_delete=models.CASCADE)


