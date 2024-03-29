from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *
from django.http import JsonResponse

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
            usuario = Usuario.objects.get(idUsuario=1)  # Substitua '1' pelo ID do usuário correto
            eventoexterno = form.save(commit=False)
            eventoexterno.nomeUsuario = usuario
            eventoexterno.save()
            #form.save()

    formularioEventoExterno = formPostagemCadastroEventoExterno()

    return render(request, "minhaAppProjetoFinal2/cadastroeventoexterno.html", {'formulario': formularioEventoExterno})

def buscarusuarios(request):
    recomendacao = Recomendacao.objects.all()
    name = 'Lista de Recomendacao Cadastrado.'
    return render(request, "minhaAppProjetoFinal2/buscarusuarios.html", {'nome': name, 'listaRecomendacao': recomendacao})

def cadastroincidenteinterno(request):
    if request.POST:
        form = formPostagemCadastroIncidenteInterno(request.POST)
        if form.is_valid():
            usuario = Usuario.objects.get(idUsuario=1)  # Substitua '1' pelo ID do usuário correto
            incidenteinterno = form.save(commit=False)
            incidenteinterno.nomeUsuario = usuario
            incidenteinterno.save()
            #form.save()

    formularioIncidenteInterno = formPostagemCadastroIncidenteInterno()
    return render(request, "minhaAppProjetoFinal2/cadastroincidenteinterno.html",{'formulario': formularioIncidenteInterno})

def lotacao(request):
    if request.POST:
        form = formPostagemCadastroLotacao(request.POST, initial={'nomeUsuario': 1})
        if form.is_valid():
            # Configurar o nomeUsuario manualmente antes de salvar o formulário
            usuario = Usuario.objects.get(idUsuario=6)  # Substitua '1' pelo ID do usuário correto
            lotacao = form.save(commit=False)
            lotacao.nomeUsuario = usuario
            lotacao.save()
            #form.save()

    formularioLotacao = formPostagemCadastroLotacao()
    return render(request, "minhaAppProjetoFinal2/lotacao.html", {'formulario': formularioLotacao})

def comentarios(request):
    filiais = Filial.objects.all()

    if request.method == 'POST':
        form = formPostagemCadastroComentario(request.POST)
        if form.is_valid():
            usuario = Usuario.objects.get(idUsuario=3)  # Substitua '3' pelo ID do usuário correto
            comentario = form.save(commit=False)
            comentario.nomeUsuario = usuario
            comentario.save()
            return redirect('comentarios')
    else:
        form = formPostagemCadastroComentario()

    # Verifica se a filial está selecionada
    filial_selecionada = request.POST.get('nomeFilial')

    if filial_selecionada:
        form.fields['nomeItem'].queryset = ItensDeConsumo.objects.filter(nomeFilial_id=filial_selecionada)
    else:
        form.fields['nomeItem'].queryset = ItensDeConsumo.objects.none()

    return render(request, "minhaAppProjetoFinal2/comentarios.html", {'formulario': form, 'filiais': filiais})

def recomendacao(request):
    if request.POST:
        form = formPostagemCadastroRecomendacao(request.POST)
        if form.is_valid():
            usuario = Usuario.objects.get(idUsuario=4)  # Substitua '1' pelo ID do usuário correto
            recomend = form.save(commit=False)
            recomend.nomeUsuario = usuario
            recomend.save()
            #form.save()

    formularioRecomendacao = formPostagemCadastroRecomendacao()
    
    return render(request, "minhaAppProjetoFinal2/recomendacao.html", {'formulario': formularioRecomendacao})

def itensDeConsumo(request):
    if request.POST:
        form = formPostagemCadastroItensDeConsumo(request.POST)
        if form.is_valid():
            usuario = Usuario.objects.get(idUsuario=4)  # Substitua '1' pelo ID do usuário correto
            item = form.save(commit=False)
            item.nomeUsuario = usuario
            item.save()
            #form.save()

    formularioLotacao = formPostagemCadastroItensDeConsumo()
    return render(request, "minhaAppProjetoFinal2/itensDeConsumo.html", {'formulario': formularioLotacao})

def exibirItens(request):
    if request.method == 'POST':
        nome_filial = request.POST.get('nomeFilial')
        print("Nome da filial selecionada:", nome_filial)

        # Obtenha a filial com base no nome selecionado
        filial = get_object_or_404(Filial, nome=nome_filial)
        print("Filial encontrada:", filial)

        # Filtrar os itens de consumo com base na filial selecionada
        itens_consumo = ItensDeConsumo.objects.filter(nomeFilial=filial)
        print("Itens de consumo filtrados:", itens_consumo)
    else:
        itens_consumo = ItensDeConsumo.objects.none()

    filiais = Filial.objects.all()

    return render(request, "minhaAppProjetoFinal2/exibirItens.html", {'filiais': filiais, 'itens_consumo': itens_consumo})

def associacaoUsuarios(request):
    if request.POST:
        form = formPostagemCadastroAssociacaoUsuarioUsuario(request.POST)
        if form.is_valid():
            usuario = Usuario.objects.get(idUsuario=4)  # Substitua '1' pelo ID do usuário correto
            associa = form.save(commit=False)
            associa.nomeUsuarioPrincipal = usuario
            associa.save()
            #form.save()

    formularioUsuarios = formPostagemCadastroAssociacaoUsuarioUsuario()
    
    return render(request, "minhaAppProjetoFinal2/associacaoUsuarios.html", {'formulario':formularioUsuarios})

def burrito(request):
    nome_item = "Burrito"  # Substitua "Arroz" pelo nome do item específico que você deseja exibir
    burritosi = ItensDeConsumo.objects.filter(nomeItem='Burrito').first()
   
    item_consumo = ItensDeConsumo.objects.filter(nomeItem=burritosi)
    comentario = Comentario.objects.filter(nomeItem=burritosi)
    # Filtrar o item de consumo com base no nome do item
    #item_consumo = get_object_or_404(ItensDeConsumo, nomeItem__nomeItem=nome_item)
    return render(request, "minhaAppProjetoFinal2/burrito.html", {'item_consumo': item_consumo, 'comentario': comentario})

def get_itens_by_filial(request):
    filial_id = request.GET.get('idFilial')
    itens_de_consumo = ItensDeConsumo.objects.filter(nomeFilial_id=filial_id).values('idItem', 'nomeItem')
    return JsonResponse(list(itens_de_consumo), safe=False)