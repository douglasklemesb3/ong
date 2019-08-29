from django.shortcuts import render
from website.models import Pessoa, Ong


# Create your views here.

def index(request):

    if request.method == 'POST':
        pessoa = Pessoa()
        pessoa.nome = request.POST.get('nome')
        pessoa.sobrenome = request.POST.get('sobrenome')
        pessoa.data_nascimento = request.POST.get('data_nascimento')
        pessoa.email = request.POST.get('email')
        pessoa.str_cep = request.POST.get('str_cep')
        pessoa.str_numero = request.POST.get('str_numero')
        pessoa.complemento = request.POST.get('complemento')
        pessoa.genero = request.POST.get('genero')
        pessoa.telefone = request.POST.get('telefone')
        pessoa.celular = request.POST.get('celular')
        pessoa.motivo = request.POST.get('motivo')
        pessoa.save()

        contexto = {
            'nome' : pessoa.nome
        }

        return render(request, 'index.html', contexto)

    return render(request, 'index.html')


def pessoas(request):
    pessoa = Pessoa.objects.filter(ativo=True).all()

    contexto = {
        'pessoas': pessoa
    }

    return render(request,'pessoas.html',contexto)


def ong(request):
    if request.method == 'POST':
        ong = Ong()
        ong.responsavel = request.POST.get('nome_responsavel')
        ong.nome = request.POST.get('nome_ong')
        ong.cep = request.POST.get('str_cep')
        ong.telefone = request.POST.get('telefone')
        ong.horario_atendimento = request.POST.get('horario_atendimento')
        ong.observacoes = request.POST.get('observacoes')

    
        contexto = {
            'responsavel' : ong.nome
        }

        return render(request, 'ongs.html', contexto)

    return render(request, 'ongs.html')



def cadastrados_ong(request):
    ong = Ong.objects.filter(ativo=True).all()

    contexto = {
        'ongs': ong
    }

    return render(request,'cadastrados_ong.html',contexto)