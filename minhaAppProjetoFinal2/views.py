from django.shortcuts import render
from .models import EventoExterno
from .models import Gerente
from .models import IncidenteInterno
from .models import Lotacao
from .models import Recomendacao
from .models import ItensDeConsumo
from .models import Comentario
from .forms import formPostagemCadastroEventoExterno
from .forms import formPostagemCadastroIncidenteInterno
from .forms import formPostagemCadastroLotacao
from .forms import formPostagemCadastroRecomendacao
from .forms import formPostagemCadastroIntensDeConsumo
from .forms import formPostagemCadastroComentario

# Create your views here.

def login(request):
    name = 'Você pode me alterar na view.'
    email = 'jhonatan99ca@hotmail.com'
    return render(request, "minhaAppProjetoFinal2/login.html", {'nome': name, 'email': email})


def cadastro(request):
    name = 'Você pode me alterar na view.'
    return render(request, "minhaAppProjetoFinal2/cadastro.html", {'nome': name})

def perfil(request):
    name = 'Você pode me alterar na view.'
    return render(request, "minhaAppProjetoFinal2/perfil.html", {'nome': name})


def meusrestaurantes(request):
    name = 'Você pode me alterar na view.'
    return render(request, "minhaAppProjetoFinal2/meusrestaurantes.html", {'nome': name})


def cadastroeventoexterno(request):
    if request.POST:
        form = formPostagemCadastroEventoExterno(request.POST)
        if form.is_valid():
            #idEvento = form.cleaned_data['idEvento']
            data = form.cleaned_data['dataEvento']
            hora = form.cleaned_data['horaEvento']
            rua = form.cleaned_data['rua']
            num = form.cleaned_data['numero']
            bairro = form.cleaned_data['bairro']
            cidade = form.cleaned_data['cidade']
            desc = form.cleaned_data['descricao']
            #idGerente =  form.cleaned_data['idGerente']
            #idUsuario  =  form.cleaned_data['idUsuario']
            #idG = Gerente.objects.get(id=idGerente)

            post = EventoExterno()

            #post.idEvento = idEvento
            #post.idEvento = idG
            post.dataEvento = data
            post.horaEvento = hora
            post.rua = rua
            post.numero = num
            post.bairro = bairro
            post.cidade = cidade
            post.descricao = desc
            #post.idGerente = idGerente
            #post.idUsuario = idUsuario

            post.save()

    formularioEventoExterno = formPostagemCadastroEventoExterno()

    return render(request, "minhaAppProjetoFinal2/cadastroeventoexterno.html", {'formulario': formularioEventoExterno})

def buscarusuarios(request):
    recomendacao = Recomendacao.objects.all()
    name = 'Lista de Recomendacao Cadastrado.'
    return render(request, "minhaAppProjetoFinal2/buscarusuarios.html", {'nome': name, 'listaRecomendacao': recomendacao})

def inserePostagem(request):
    """if request.POST:
        form = formPostagem(request.POST)
        if form.is_valid():
            tit = form.cleaned_data['titulo']
            tex = form.cleaned_data['texto']
            dh = form.cleaned_data['data']

            post = postagem()
            post.titulo = tit
            post.texto = tex
            post.data = dh

            post.save()

    formulario = formPostagem()

    return render(request, "minhaAppProjetoFinal2/inserePostagem.html", {'formulario': formulario})"""
    name = 'Insere Postagem.'
    return render(request, "minhaAppProjetoFinal2/inserePostagem.html", {'nome': name})

def cadastroincidenteinterno(request):
    if request.POST:
        form = formPostagemCadastroIncidenteInterno(request.POST)
        if form.is_valid():
            #idEvento = form.cleaned_data['idEvento']
            data = form.cleaned_data['data']
            hora = form.cleaned_data['hora']
            local = form.cleaned_data['local']
            desc = form.cleaned_data['descricao']
            #idGerente = form.cleaned_data['idGerente']
            #idUsuario  = form.cleaned_data['idUsuario']
            #idG = Gerente.objects.get(id=idGerente)

            post = IncidenteInterno()

            #post.idEvento = idEvento
            #post.idEvento = idG
            post.data = data
            post.hora = hora
            post.local = local
            post.descricao = desc

            #post.idGerente = idGerente
            #post.idUsuario = idUsuario

            post.save()

    formularioIncidenteInterno = formPostagemCadastroIncidenteInterno()
    return render(request, "minhaAppProjetoFinal2/cadastroincidenteinterno.html",{'formulario': formularioIncidenteInterno})


def lotacao(request):
    if request.POST:
        form = formPostagemCadastroLotacao(request.POST)
        if form.is_valid():
            #idLotacao = form.cleaned_data['idLotacao']
            data = form.cleaned_data['dia']
            hora = form.cleaned_data['hora']
            faixa = form.cleaned_data['faixaHoraria']
            #idGerente = form.cleaned_data['idGerente']
            #idUsuario  = form.cleaned_data['idUsuario']
            #idNivel = form.cleaned_data['idNivel']
            #idFilial  = form.cleaned_data['idFilial']
            #idG = Gerente.objects.get(id=idGerente)

            post = Lotacao()

            #post.idEvento = idEvento
            #post.idEvento = idG
            post.dia = data
            post.hora = hora
            post.faixaHoraria = faixa
            
            #post.idGerente = idGerente
            #post.idUsuario = idUsuario
            #post.idNivel = idNivel
            #post.idFilial = idFilial

            post.save()

    formularioLotacao = formPostagemCadastroLotacao()
    return render(request, "minhaAppProjetoFinal2/lotacao.html", {'formulario': formularioLotacao})


def comentarios(request):
    if request.POST:
        form = formPostagemCadastroComentario(request.POST)
        if form.is_valid():
            #idComentario = form.cleaned_data['idComentario']
            data = form.cleaned_data['data']
            hora = form.cleaned_data['hora']
            conteudo = form.cleaned_data['conteudo']

            post = Comentario()

            post.data = data
            post.hora = hora
            post.conteudo = conteudo

            post.save()

    formularioComentario = formPostagemCadastroComentario()
    return render(request, "minhaAppProjetoFinal2/comentarios.html", {'formulario': formularioComentario})


def recomendacao(request):
    if request.POST:
        form = formPostagemCadastroRecomendacao(request.POST)
        if form.is_valid():
            #idRecomendacao = form.cleaned_data['idRecomendacao']
            data = form.cleaned_data['data']
            hora = form.cleaned_data['hora']
            texto = form.cleaned_data['texto']
            #idUsuario  = form.cleaned_data['idUsuario']
            #idFilial  = form.cleaned_data['idFilial']

            post = Recomendacao()

            #post.idEvento = idEvento
            #post.idEvento = idG
            post.data = data
            post.hora = hora
            post.texto = texto
            
            #post.idUsuario = idUsuario
            #post.idFilial = idFilial

            post.save()

    formularioRecomendacao = formPostagemCadastroRecomendacao()
    
    return render(request, "minhaAppProjetoFinal2/recomendacao.html", {'formulario': formularioRecomendacao})

def exibirEventoExterno(request):
    listaEventoExterno = EventoExterno.objects.all()
    name = 'Lista de Inicidente Interno Cadastrado.'
    return render(request, "minhaAppProjetoFinal2/exibirEventoExterno.html", {'listaEventoExterno': listaEventoExterno})


def exibirincidenteinterno(request):
    listaIncidenteInterno = IncidenteInterno.objects.all()
    name = 'Lista de Inicidente Interno Cadastrado.'
    return render(request, "minhaAppProjetoFinal2/exibirincidenteinterno.html", {'nome': name, 'listaIncidenteInterno': listaIncidenteInterno})


def exibirlotacao(request):
    name='Você pode me alterar na view.'
    return render(request, "minhaAppProjetoFinal2/exibirlotacao.html", {'nome':name})


def exibirRecomendacao(request):
    recomendacao = Recomendacao.objects.all()
    name = 'Lista de Recomendacao Cadastrado.'
    return render(request, "minhaAppProjetoFinal2/exibirRecomendacao.html", {'nome': name, 'listaRecomendacao': recomendacao})


def exibirComentario(request):
    comentario = Comentario.objects.all()
    name = 'Lista de Comentário Cadastrado.'
    return render(request, "minhaAppProjetoFinal2/exibirComentario.html", {'nome': name, 'listaComentario': comentario})

