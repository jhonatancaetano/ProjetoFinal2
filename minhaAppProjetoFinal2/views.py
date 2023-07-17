from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *

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
            form.save()

    formularioIncidenteInterno = formPostagemCadastroIncidenteInterno()
    return render(request, "minhaAppProjetoFinal2/cadastroincidenteinterno.html",{'formulario': formularioIncidenteInterno})

def lotacao(request):
    if request.POST:
        form = formPostagemCadastroLotacao(request.POST)
        if form.is_valid():
            form.save()

    formularioLotacao = formPostagemCadastroLotacao()
    return render(request, "minhaAppProjetoFinal2/lotacao.html", {'formulario': formularioLotacao})


def comentarios(request):
    if request.POST:
        form = formPostagemCadastroComentario(request.POST)
        if form.is_valid():
            form.save()

    formularioComentario = formPostagemCadastroComentario()
    return render(request, "minhaAppProjetoFinal2/comentarios.html", {'formulario': formularioComentario})

def recomendacao(request):
    if request.POST:
        form = formPostagemCadastroRecomendacao(request.POST)
        if form.is_valid():
            form.save()

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

def itensDeConsumo(request):
    if request.POST:
        form = formPostagemCadastroItensDeConsumo(request.POST)
        if form.is_valid():
            form.save()

    formularioLotacao = formPostagemCadastroItensDeConsumo()
    return render(request, "minhaAppProjetoFinal2/itensDeConsumo.html", {'formulario': formularioLotacao})

def exibirItens(request):
    if request.method == 'POST':
        id_filial = request.POST.get('idFilial')
        idFilial = Filial.objects.get(idFilial=id_filial)
        itens_consumo = ItensDeConsumo.objects.filter(idFilial=idFilial)
    else:
        itens_consumo = ItensDeConsumo.objects.none()  # Retorna uma queryset vazia

    filiais = Filial.objects.all()
    
    return render(request, "minhaAppProjetoFinal2/exibirItens.html", {'filiais': filiais, 'itens_consumo': itens_consumo})

def editarincidenteinterno(request, pk):
    incidente = get_object_or_404(IncidenteInterno, pk=pk)

    if request.method == 'POST':
        form = formPostagemCadastroIncidenteInterno(request.POST, instance=incidente)
        if form.is_valid():
            form.save()
            return redirect('cadastroincidenteinterno')  # Redirecione para a página de listagem de incidentes internos ou outra página adequada após a edição

    form = formPostagemCadastroIncidenteInterno(instance=incidente)
    return render(request, 'minhaAppProjetoFinal2/editarincidenteinterno.html', {'formulario': form})

def associacaoUsuarios(request):
    if request.POST:
        form = formPostagemCadastroAssociacaoUsuarioUsuario(request.POST)
        if form.is_valid():
            form.save()

    formularioUsuarios = formPostagemCadastroAssociacaoUsuarioUsuario()
    
    return render(request, "minhaAppProjetoFinal2/associacaoUsuarios.html", {'formulario':formularioUsuarios})