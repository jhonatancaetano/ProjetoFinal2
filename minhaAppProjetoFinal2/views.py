from django.shortcuts import render

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

