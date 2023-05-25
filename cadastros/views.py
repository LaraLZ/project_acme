from django.shortcuts import render
from cadastros.models import Empresas_afiliacao, Empresas
from django.http.response import HttpResponse
import json
# Create your views here.
#
def empresas(request):
   
    empresas = Empresas.objects.all().values('empresa','status', 'id')
    return render(request, 'empresas.html',{'empresas':empresas})


#caso o metodo de requisiçao for post, irá ser insirido novas informacoes na tabela do banco de dados e ira renderizar a pagina do acadastros.html ,se nao, ira apenas renderizar a pagina cadastro.html
def cadastros(request):
    if request.method == "POST":#está verificando se  o metodo de requisicao é igual a post
        print(request.POST) #a funcao print serve para imprimir tudo que esta dentro do parenteses no terminal.
        if request.POST["ativo"] == "sim":#ele verifica se o ativo é igual a sim        
            ativo = True #define a variavel ativo como verdadeiro
        else: #caso o a 1 condicao nao seja verdadeira 
            ativo = False #o ativo é falso
        Empresas_afiliacao.objects.create(#empresa_afiliacao é uma tabela no banco/ .create cria uma nova linha/cadastro
            cnpj = int(request.POST["cnpj"]),#identifica uma coluna no banco com o nome cnpj e inseri um valor
            afiliacao = request.POST["nome"],#identifica uma coluna com o nome afiliacao e coloca um valor
            status = ativo,#identifica o nome status e insire o valor (True/False) correspondente da verificacao da linha 10
            empresa_id = request.POST["empresa"]
        )
        empresa = Empresas.objects.get(id = request.POST["empresa"])
        return render(request, 'cadastros.html',{
            'empresa':empresa.empresa,
            'status':empresa.status,
            'id':empresa.id,
            })#retorna a rederizacao do (cadatros.html)
    else:#caso o metodo de requisicao nao for igual a post vai ser executado o else
        return render(request, 'cadastros.html')#retorna a rederizacao dos codigos html (cadastros.html)
    #models==cadastros_empresas

def empresa_editar(request, id):
    if request.method == "GET":
        empresa = Empresas.objects.get(id = id)

        return render(request, 'cadastros.html', {
            'empresa':empresa.empresa,
            'status':empresa.status,
            'id':empresa.id,
        })
    else:
        if request.POST["ativo"] == "sim":# 
            ativo = True
        else:
            ativo = False
        Empresas.objects.filter(id=id).update(
            empresa = request.POST["empresa"],
            status = ativo,
        )

        empresas = Empresas.objects.all().values('empresa','status', 'id')
        return render(request, 'empresas.html',{'empresas':empresas})


    
def criar_empresa(request):
    if request.method == "GET":
        return render(request, 'criar_empresa.html')
    if request.method == "POST":
        print(request.POST)
        if request.POST["ativo"] == "sim":# 
            ativo = True
        else:
            ativo = False
        empresa_criar = Empresas(
            empresa = request.POST["empresa"],
            status = ativo,
        )
        empresa_criar.save()

        return render(request, 'cadastros.html', {
            'empresa':empresa_criar.empresa,
            'status':empresa_criar.status,
            'id':empresa_criar.id,
            })
#pagina inicial
#novo

def listar_cnpj(request):
    from django.core import serializers
    if request.method == "GET":
        print(request.GET)
        id = request.GET.get('id')
        print(id)
        buscar_cnpj = Empresas_afiliacao.objects.filter(empresa_id = id)
        print(buscar_cnpj)
        if not buscar_cnpj:
            buscar_cnpj = ''


        data = serializers.serialize("python", Empresas_afiliacao.objects.filter(empresa_id = id))
        return HttpResponse(json.dumps(data), content_type="application/json")
#buscar afiliacao

def deletar_cnpj(request, id):
    if request.method == 'GET':
        cnpj = Empresas_afiliacao.objects.get(id = id)
        empresa = Empresas.objects.get(id = cnpj.empresa.id)
        cnpj.delete()

        return render(request, 'cadastros.html', {
            'empresa':empresa.empresa,
            'status':empresa.status,
            'id':empresa.id,
            })
    
def deletar_empresa(request, id):
    if request.method == 'GET':
        empresa = Empresas.objects.get(id = id)
        empresa.delete()
        return render(request, 'empresas.html')