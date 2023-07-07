from django.shortcuts import render
from .models import EventoExterno
from .models import Gerente
from .forms import formPostagemCadastroEventoExterno

# Create your views here.

def login(request):
    name='Você pode me alterar na view.'
    email='jhonatan99ca@hotmail.com'
    return render(request, "minhaAppProjetoFinal2/login.html", {'nome':name, 'email':email})


def cadastro(request):
    name='Você pode me alterar na view.'
    return render(request, "minhaAppProjetoFinal2/cadastro.html", {'nome':name})

def perfil(request):
    name='Você pode me alterar na view.'
    return render(request, "minhaAppProjetoFinal2/perfil.html", {'nome':name})


def meusrestaurantes(request):
    name='Você pode me alterar na view.'
    return render(request, "minhaAppProjetoFinal2/meusrestaurantes.html", {'nome':name})


def cadastroeventoexterno(request):
    if request.POST:
        form = formPostagemCadastroEventoExterno(request.POST)
        if form.is_valid():
            #idEvento = form.cleaned_data['idEvento']
            data = form.cleaned_data['dataEvento']
            hora = form.cleaned_data['horaEvento']
            rua = form.cleaned_data['rua']
            num =  form.cleaned_data['numero']
            bairro = form.cleaned_data['bairro']
            cidade = form.cleaned_data['cidade']
            desc =  form.cleaned_data['descricao']
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

    return render(request, "minhaAppProjetoFinal2/cadastroeventoexterno.html", {'formulario':formularioEventoExterno})

def buscarusuarios(request):
    listaEventoExterno = EventoExterno.objects.all()
    name='Lista de Evento Externo Cadastrado.'
    return render(request, "minhaAppProjetoFinal2/buscarusuarios.html", {'nome':name, 'listaEventoExterno':listaEventoExterno})

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

    return render(request, "minhaAppProjetoFinal2/inserePostagem.html", {'nome':name})
