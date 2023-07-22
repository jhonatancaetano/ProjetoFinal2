from django.db import models

# Create your models here.

class TipoDeComida(models.Model):
    idComida = models.AutoField(primary_key=True)
    descComida = models.TextField()
    def __str__(self):
        return str(self.descComida)

class Restaurante(models.Model):
    idRestaurante = models.AutoField(primary_key=True)
    nome = models.TextField()
    Comida = models.ForeignKey("TipoDeComida", on_delete=models.CASCADE)
    def __str__(self):
        return str(self.nome)

class Filial(models.Model):
    idFilial = models.AutoField(primary_key=True)
    nome = models.TextField()
    rua = models.TextField()
    numero = models.IntegerField()
    nomeRestaurante = models.ForeignKey("Restaurante", on_delete=models.CASCADE)
    def __str__(self):
        return str(self.nome)

class Gerente(models.Model):
    idGerente = models.AutoField(primary_key=True)
    Filial = models.ForeignKey("Filial", on_delete=models.CASCADE)
    nomeUsuario = models.ForeignKey("Usuario", on_delete=models.CASCADE)
    def __str__(self):
        return str(self.idGerente)

class RevisaoDeComentario(models.Model):
    idRevisao = models.AutoField(primary_key=True)
    data = models.DateField()
    hora = models.TimeField()
    conteudo = models.TextField()
    def __str__(self):
        return str(self.idRevisao)

class ClassificacaoDoItem(models.Model):
    idClassificacao = models.AutoField(primary_key=True)
    descItem = models.TextField()
    def __str__(self):
        return str(self.descItem)

class ItensDeConsumo(models.Model):
    idItem = models.AutoField(primary_key=True)
    nomeItem = models.TextField()
    precoItem = models.FloatField()
    nomeFilial = models.ForeignKey("Filial", on_delete=models.CASCADE)
    nomeClassificacao = models.ForeignKey("ClassificacaoDoItem", on_delete=models.CASCADE)
    nomeUsuario = models.ForeignKey("Usuario", on_delete=models.CASCADE)
    def __str__(self):
        return str(self.nomeItem)
    
class Comentario(models.Model):
    idComentario = models.AutoField(primary_key=True)
    data = models.DateField()
    hora = models.TimeField()
    conteudo = models.TextField()
    nomeFilial = models.ForeignKey("Filial", on_delete=models.CASCADE)
    nomeItem = models.ForeignKey("ItensDeConsumo", on_delete=models.CASCADE)
    nomeUsuario = models.ForeignKey("Usuario", on_delete=models.CASCADE)
    def __str__(self):
        return str(self.idComentario)

class TipoDeRelacionamento(models.Model):
    idTipoRelacionamento = models.AutoField(primary_key=True)
    descTipoRelacionamento = models.TextField()
    def __str__(self):
        return str(self.descTipoRelacionamento)
    
class Relacionamento(models.Model):
    idRelacionamento = models.AutoField(primary_key=True)
    nomeTipoRelacionamento = models.ForeignKey("TipoDeRelacionamento", on_delete=models.CASCADE)
    def __str__(self):
        return str(self.idRelacionamento)

class Usuario(models.Model):
    idUsuario = models.AutoField(primary_key=True)
    nome = models.TextField()
    numeroTelefone = models.IntegerField()
    email = models.EmailField(max_length=254)
    senha = models.TextField()
    cpf = models.IntegerField()
    def __str__(self):
        return str(self.nome)

class NivelDeLotacao(models.Model):
    idNivel = models.AutoField(primary_key=True)
    descNivel = models.TextField()
    def __str__(self):
        return str(self.descNivel)

class Lotacao(models.Model):
    idLotacao = models.AutoField(primary_key=True)
    dia = models.DateField()
    hora = models.TimeField()
    nomeNivel = models.ForeignKey("NivelDeLotacao", on_delete=models.CASCADE)
    nomeFilial = models.ForeignKey("Filial", on_delete=models.CASCADE)
    nomeUsuario = models.ForeignKey("Usuario", on_delete=models.CASCADE)
    def __str__(self):
        return str(self.idLotacao)

class TipoDeIncidenteInterno(models.Model):
    idTipoIncidente = models.AutoField(primary_key=True)
    descIncidente = models.TextField()
    def __str__(self):
        return str(self.descIncidente)

class IncidenteInterno(models.Model):    
    idIncidente = models.AutoField(primary_key=True)
    data = models.DateField()
    hora = models.TimeField()
    descricao = models.TextField()
    nomeFilial = models.ForeignKey("Filial", on_delete=models.CASCADE)
    nomeTipoDeIncidente = models.ForeignKey("TipoDeIncidenteInterno", on_delete=models.CASCADE)
    nomeUsuario = models.ForeignKey("Usuario", on_delete=models.CASCADE)
    def __str__(self):
        return str(self.idIncidente)

class EventoExterno(models.Model):
    idEvento = models.AutoField(primary_key=True)
    dataEvento = models.DateField()
    horaEvento = models.TimeField()
    rua = models.TextField()
    numero = models.IntegerField()
    bairro = models.TextField()
    cidade = models.TextField()
    descricao = models.TextField()
    nomeUsuario = models.ForeignKey("Usuario", on_delete=models.CASCADE)
    def __str__(self):
        return str(self.idEvento)

class Recomendacao(models.Model):
    idRecomendacao = models.AutoField(primary_key=True)
    data = models.DateField()
    hora = models.TimeField()
    texto = models.TextField()
    nomeFilial = models.ForeignKey("Filial", on_delete=models.CASCADE)
    nomeUsuario = models.ForeignKey("Usuario", on_delete=models.CASCADE)
    def __str__(self):
        return str(self.idRecomendacao)

class AssociacaoFilialEventoExterno(models.Model):
    nomeFilial = models.ForeignKey("Filial", on_delete=models.CASCADE)
    nomeEvento = models.ForeignKey("EventoExterno", on_delete=models.CASCADE)

class AssociacaoItemDeConsumoRecomendacao(models.Model):
    nomeRecomendacao = models.ForeignKey("Recomendacao", on_delete=models.CASCADE)
    nomeItem = models.ForeignKey("ItensDeConsumo", on_delete=models.CASCADE)

class AssociacaoRestauranteUsuario(models.Model):
    nomeRestaurante = models.ForeignKey("Restaurante", on_delete=models.CASCADE)
    nomeUsuario = models.ForeignKey("Usuario", on_delete=models.CASCADE)

class AssociacaoUsuarioUsuario(models.Model):
    nomeUsuarioPrincipal = models.ForeignKey("Usuario", on_delete=models.CASCADE, related_name='associacao_usuario1')
    nomeUsuarioSecundario = models.ForeignKey("Usuario", on_delete=models.CASCADE, related_name='associacao_usuario2')
    nomeTipoRelacionamento = models.ForeignKey("TipoDeRelacionamento", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nomeUsuarioPrincipal} - {self.nomeUsuarioSecundario} - {self.nomeTipoRelacionamento}"

    class Meta:
        # Definindo a chave primรกria concatenada
        constraints = [
            models.UniqueConstraint(fields=['nomeUsuarioPrincipal', 'nomeUsuarioSecundario', 'nomeTipoRelacionamento'], name='chave_primaria_concatenada')
        ]
