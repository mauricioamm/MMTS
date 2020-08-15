from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import admin
from django.db import connection
import datetime
import csv
from django.contrib.auth.views import LogoutView
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User
from django.db.models import Count
from random import randint
from django.contrib.auth.decorators import login_required
from .models import Cond1Bloco01Model, BlocoSaidaModel, TodosOsBlocos, ParticipanteModel
from .forms import Cond1Bloco01Form, BlocoSaidaForm

from django.db import migrations
from django.apps import apps
from django.db import models
import wave
from django.template import loader
from django.core import serializers
from django.http import JsonResponse
import json

# def LogoutView(request):
#    logout(request)

#def carregar_modelo():
#    print('')

def ResetSaida(request):
    user = request.user
    banquinho = str(user)
    objeto_saida= BlocoSaidaModel.objetos.using(banquinho).all().delete()
    #objeto_saida.save()
    objeto_novo = BlocoSaidaModel.objetos.using(banquinho).get_or_create(id='1')

def inserir_registro_saida(request):
    user = request.user
    banquinho = str(user)
    objeto_saida = BlocoSaidaModel.objetos.using(banquinho).last()
    n_saida_ultimo = objeto_saida.id
    pk_next = n_saida_ultimo + 1
    objeto_saida.pk = None
    objeto_saida.pk = pk_next
    objeto_saida.save()
    #-------gravar saida default
    objeto_saida.Acertou = '0'
    objeto_saida.save()
    print('novo pk_next, com inserir_registro_saida', pk_next)

def Entrada_login(request):
    usuario = request.user
    if request.POST.get('visitante'):
        #request.user = User.objects.get(username='visitante')
        usuario = User(username='visitante')
        #u = User.objects.get(username='visitante')
        #u.save()
    context= {
            "user": usuario
    }
    return render(request, "MtsApp/Entrada_login.html", context)

def Entrada(request):
    return render(request, "MtsApp/Entrada.html")

def Comecar_bloco(request):
    user = request.user
    banquinho = str(user)
    objeto_saida = BlocoSaidaModel.objetos.using(banquinho).last()
    # objeto_saida = BlocoSaidaModel.objetos.using(banquinho).get(pk=1)
    form = BlocoSaidaForm(request.POST or None, instance=objeto_saida)

    # localizar bloco
    objeto_participante = ParticipanteModel.objetos.using(banquinho).get(pk=1)
    nqualbloco = objeto_participante.NoBlocoProximo
    objeto_TodosOsBlocos = TodosOsBlocos.objetos.using(banquinho).get(NoBloco=nqualbloco)
    xqualbloco = objeto_TodosOsBlocos.NomeBloco
    model_name = apps.get_model("MtsApp", xqualbloco)
    objeto_bloco = model_name.objetos.using(banquinho).get(pk=1)

    # Preencher próximo registro de saída
    quantos_saida = BlocoSaidaModel.objetos.using(banquinho).count()
    if quantos_saida == 1:
        objeto_saida = BlocoSaidaModel.objetos.using(banquinho).get(pk=1)
    elif quantos_saida > 1:
        # ---- registros que não são mais atuais:
        listax = BlocoSaidaModel.objetos.using(banquinho)
        for item in listax:
            item.SeBlocoAtual = '0'
            item.save()
            print(item)
        n_saida_ultimo = objeto_saida.id
        pk_next = n_saida_ultimo + 1
        objeto_saida.pk = None
        objeto_saida.pk = pk_next
        objeto_saida.save()

    # -------gravar saida default
    objeto_saida.Acertou = '0'
    objeto_saida.Corretas = '0'
    objeto_saida.Porcentagem = '0'
    objeto_saida.SeBlocoAtual = '1'
    objeto_saida.Dia = str(datetime.date.today())
    objeto_saida.NomeBloco = objeto_bloco.NomeBloco
    objeto_saida.Ordem = objeto_bloco.Ordem
    objeto_saida.Tentativa = objeto_bloco.Tentativa
    objeto_saida.TipoTentativa = objeto_bloco.TipoTentativa
    objeto_saida.Modelo = objeto_bloco.Modelo
    objeto_saida.SupEsq = objeto_bloco.SupEsq
    objeto_saida.SupDir = objeto_bloco.SupDir
    objeto_saida.InfEsq = objeto_bloco.InfEsq
    objeto_saida.InfDir = objeto_bloco.InfDir
    objeto_saida.Reforco = objeto_bloco.Reforco
    objeto_saida.Correta = objeto_bloco.Correta
    objeto_saida.Horario = datetime.datetime.now().strftime('%H:%M:%S')
    objeto_saida.save()

    ContadorRegistrosAtuais = BlocoSaidaModel.objetos.using(banquinho).filter(SeBlocoAtual='1').count()
    numero = ContadorRegistrosAtuais
    context = {
        'objeto_bloco': objeto_bloco,
        'form': form,
        'numero': numero,
    }
    return render(request, 'MtsApp/ComecarBloco.html', context)



#@login_required
def Entrada_Iniciar(request):
    user = request.user
    banquinho = str(user)

    if request.POST.get('comecar_sessao'):
        user = request.user
        banquinho = str(user)
        objeto_saida = BlocoSaidaModel.objetos.using(banquinho).last()
        #objeto_saida = BlocoSaidaModel.objetos.using(banquinho).get(pk=1)
        form = BlocoSaidaForm(request.POST or None, instance=objeto_saida)

        # localizar bloco
        objeto_participante= ParticipanteModel.objetos.using(banquinho).get(pk=1)
        nqualbloco= objeto_participante.NoBlocoProximo
        objeto_TodosOsBlocos = TodosOsBlocos.objetos.using(banquinho).get(NoBloco=nqualbloco)
        xqualbloco = objeto_TodosOsBlocos.NomeBloco
        model_name = apps.get_model("MtsApp", xqualbloco)
        objeto_bloco = model_name.objetos.using(banquinho).get(pk=1)

        # Preencher próximo registro de saída
        quantos_saida = BlocoSaidaModel.objetos.using(banquinho).count()
        if quantos_saida == 1:
            objeto_saida = BlocoSaidaModel.objetos.using(banquinho).get(pk=1)
        elif quantos_saida > 1:
            # ---- registros que não são mais atuais:
            listax = BlocoSaidaModel.objetos.using(banquinho)
            for item in listax:
                item.SeBlocoAtual= '0'
                item.save()
                print(item)
            n_saida_ultimo = objeto_saida.id
            pk_next = n_saida_ultimo + 1
            objeto_saida.pk = None
            objeto_saida.pk = pk_next
            objeto_saida.save()

        # -------gravar saida default
        objeto_saida.Acertou = '0'
        objeto_saida.Corretas = '0'
        objeto_saida.Porcentagem = '0'
        objeto_saida.SeBlocoAtual= '1'
        objeto_saida.Dia = str(datetime.date.today())
        objeto_saida.NomeBloco = objeto_bloco.NomeBloco
        objeto_saida.Ordem = objeto_bloco.Ordem
        objeto_saida.Tentativa = objeto_bloco.Tentativa
        objeto_saida.TipoTentativa = objeto_bloco.TipoTentativa
        objeto_saida.Modelo = objeto_bloco.Modelo
        objeto_saida.SupEsq = objeto_bloco.SupEsq
        objeto_saida.SupDir = objeto_bloco.SupDir
        objeto_saida.InfEsq = objeto_bloco.InfEsq
        objeto_saida.InfDir = objeto_bloco.InfDir
        objeto_saida.Reforco = objeto_bloco.Reforco
        objeto_saida.Correta = objeto_bloco.Correta
        objeto_saida.Horario = datetime.datetime.now().strftime('%H:%M:%S')
        #objeto_saida.Ordem = '1'
        objeto_saida.save()

        ContadorRegistrosAtuais = BlocoSaidaModel.objetos.using(banquinho).filter(SeBlocoAtual='1').count()
        numero = ContadorRegistrosAtuais
        context= {
            'objeto_bloco': objeto_bloco,
            'form': form,
            'numero': numero,
        }
        return render(request, 'MtsApp/ComecarBloco.html', context)
    return render(request, "MtsApp/Entrada_iniciar.html")

@staff_member_required
def Entrada_configuracoes(request):
    if request.POST.get('ResetSaida'):
        #----Resetando
        user = request.user
        banquinho = str(user)
        objeto_apagar = BlocoSaidaModel.objetos.using(banquinho).all()
        objeto_apagar.delete()
        # objeto_saida.save()

        #----Inserindo primeiro registro de saída
        objeto_saida, created = BlocoSaidaModel.objetos.using(banquinho).get_or_create(
            id='1',
            Ordem= '1',
            Corretas='0',
            Porcentagem='0',
            Participante= banquinho,
        )
        objeto_saida.save()
        SeApagou= 'OK. Registros apagados'
        context={
            'resultado': SeApagou
        }
        return render(request, "MtsApp/Entrada_configuracoes.html", context)
    SeApagou = ''
    context = {
        'resultado': SeApagou
    }
    return render(request, "MtsApp/Entrada_configuracoes.html", context)

@staff_member_required
def Entrada_relatorios(request):
    user = request.user
    banquinho = str(user)
    if request.POST.get('export'):
        #listax = SessaoModel.objetos.using(banquinho).all()
        #listax = SessaoModel.objetos.using(banquinho).values()
        listax= BlocoSaidaModel.objetos.using(banquinho).values_list(
            'id', 'NomeBloco', 'Participante', 'Ordem', 'Tentativa', 'Modelo', 'SupDir', 'InfEsq', 'InfDir', 'Reforco',
            'Correta', 'Escolheu', 'Acertou', 'RespVerb', 'Dia', 'Horario', 'Sessao', 'Corretas', 'Porcentagem',
            'Procedimento')

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="MTS_saida.csv"'
        writer = csv.writer(response)
        writer.writerow([ 'id', 'NomeBloco', 'Participante', 'Ordem', 'Tentativa', 'Modelo', 'SupDir', 'InfEsq', 'InfDir', 'Reforco',
            'Correta', 'Escolheu', 'Acertou', 'RespVerb', 'Dia',
                          'Horario', 'Sessao', 'Corretas', 'Porcentagem',
            'Procedimento'])
        for item in listax:
            print(item)
            writer = csv.writer(response)
            writer.writerow([item])
        return response

    return render(request, "MtsApp/Entrada_relatorios.html")

def Entrada_sobre(request):
    return render(request, "MtsApp/Entrada_sobre.html")

#def LogoutView(request):
#    logout(request)

def QualBanquinho(request):
    user = request.user
    banquinho = str(user)
    return(banquinho)

def SeAcertou(request):
    #---SeAcertou-----------------------
    user = request.user
    banquinho = str(user)
    objeto_saida = BlocoSaidaModel.objetos.using(banquinho).last()

    # localizar bloco
    objeto_participante = ParticipanteModel.objetos.using(banquinho).get(pk=1)
    nqualbloco = objeto_participante.NoBlocoProximo
    objeto_TodosOsBlocos = TodosOsBlocos.objetos.using(banquinho).get(NoBloco=nqualbloco)
    xqualbloco = objeto_TodosOsBlocos.NomeBloco
    print('Se deu certo, pegamos o bloco:', xqualbloco)
    model_name = apps.get_model("MtsApp", xqualbloco)
    objeto_bloco = model_name.objetos.using(banquinho).get(pk=1)

    objeto_bloco_ultimo = model_name.objetos.using(banquinho).last()
    total = objeto_bloco_ultimo.id

    n_objeto_saida = BlocoSaidaModel.objetos.using(banquinho).filter(SeBlocoAtual='1').count()
    #n_objeto_saida = objeto_saida.id
    #xqualbloco= 'Cond1Bloco01Model'
    #model_name = apps.get_model("MtsApp", xqualbloco)
    objeto_bloco= model_name.objetos.using(banquinho).get(pk=n_objeto_saida)

    if objeto_bloco.Correta == objeto_saida.Escolheu:
        objeto_saida.Acertou = '1'
        print('parece que acertou')
        #SomAcertou = open('acertou.mp3',"rb")
        #SomAcertou.read()
        #SomAcertou = open('/static/MtsApp/sons/acertou2.wav')
        XCorretas = objeto_saida.Corretas
        NCorretas = int(XCorretas)
        NCorretas += 1
        objeto_saida.Corretas = str(NCorretas)

        Porcent = int(NCorretas * 100 / total)
        objeto_saida.Porcentagem = str(Porcent)
        objeto_saida.save()

def gravar_saida(request):
    user = request.user
    banquinho = str(user)
    objeto_saida= BlocoSaidaModel.objetos.using(banquinho).last()
    n_objeto_saida = objeto_saida.id

    # localizar bloco
    objeto_participante = ParticipanteModel.objetos.using(banquinho).get(pk=1)
    nqualbloco = objeto_participante.NoBlocoProximo
    objeto_TodosOsBlocos = TodosOsBlocos.objetos.using(banquinho).get(NoBloco=nqualbloco)
    xqualbloco = objeto_TodosOsBlocos.NomeBloco
    print('Se deu certo, pegamos o bloco:', xqualbloco)
    model_name = apps.get_model("MtsApp", xqualbloco)
    objeto_bloco = model_name.objetos.using(banquinho).get(pk=1)

    objeto_bloco= model_name.objetos.using(banquinho).get(pk=n_objeto_saida)
    objeto_saida.Dia = str(datetime.date.today())
    objeto_saida.NomeBloco =    objeto_bloco.NomeBloco
    objeto_saida.Ordem =        objeto_bloco.Ordem
    objeto_saida.Tentativa =    objeto_bloco.Tentativa
    objeto_saida.TipoTentativa = objeto_bloco.TipoTentativa
    objeto_saida.Modelo =       objeto_bloco.Modelo
    objeto_saida.SupEsq =       objeto_bloco.SupEsq
    objeto_saida.SupDir =       objeto_bloco.SupDir
    objeto_saida.InfEsq =       objeto_bloco.InfEsq
    objeto_saida.InfDir =       objeto_bloco.InfDir
    objeto_saida.Reforco =      objeto_bloco.Reforco
    objeto_saida.Correta =      objeto_bloco.Correta
    objeto_saida.Horario =      datetime.datetime.now().strftime('%H:%M:%S')
    objeto_saida.save()

def supesq_view(request):
    user = request.user
    banquinho = str(user)
    objeto_saida = BlocoSaidaModel.objetos.using(banquinho).last()
    ContadorRegistrosAtuais = BlocoSaidaModel.objetos.using(banquinho).filter(SeBlocoAtual='1').count()
    numero = ContadorRegistrosAtuais
    # objeto_saida_ultimo = BlocoSaidaModel.objetos.using(banquinho).last()
    objeto_saida.Escolheu = '1'
    objeto_saida.save()

    # ---SeAcertou-----------------------
    user = request.user
    banquinho = str(user)
    objeto_saida = BlocoSaidaModel.objetos.using(banquinho).last()

    # localizar bloco
    objeto_participante = ParticipanteModel.objetos.using(banquinho).get(pk=1)
    nqualbloco = objeto_participante.NoBlocoProximo
    objeto_TodosOsBlocos = TodosOsBlocos.objetos.using(banquinho).get(NoBloco=nqualbloco)
    xqualbloco = objeto_TodosOsBlocos.NomeBloco
    print('Se deu certo, pegamos o bloco:', xqualbloco)
    model_name = apps.get_model("MtsApp", xqualbloco)
    objeto_bloco = model_name.objetos.using(banquinho).get(pk=1)

    objeto_bloco_ultimo = model_name.objetos.using(banquinho).last()
    total = objeto_bloco_ultimo.id
    n_objeto_saida = BlocoSaidaModel.objetos.using(banquinho).filter(SeBlocoAtual='1').count()
    #n_objeto_saida = objeto_saida.id
    objeto_bloco = model_name.objetos.using(banquinho).get(pk=n_objeto_saida)

    if objeto_bloco.Correta == objeto_saida.Escolheu:
        objeto_saida.Acertou = '1'
        print('parece que acertou')
        # SomAcertou = open('acertou.mp3',"rb")
        # SomAcertou.read()
        # SomAcertou = open('/static/MtsApp/sons/acertou2.wav')
        XCorretas = objeto_saida.Corretas
        NCorretas = int(XCorretas)
        NCorretas += 1
        objeto_saida.Corretas = str(NCorretas)

        Porcent = int(NCorretas * 100 / total)
        objeto_saida.Porcentagem = str(Porcent)
        objeto_saida.ErroTipo = ''
        objeto_saida.save()
    else:
        objeto_saida.Acertou = '0'
        if objeto_bloco.TipoTentativa == "tipo1":
            objeto_saida.ErroTipo= 'errotipo1'
            objeto_saida.save()
        elif objeto_bloco.TipoTentativa == "tipo2":
            objeto_saida.ErroTipo = 'errotipo2'
            objeto_saida.save()
        elif objeto_bloco.TipoTentativa == "tipo3":
            objeto_saida.ErroTipo = 'errotipo3'
            objeto_saida.save()
        objeto_saida.save()

    #----gravar_saida
    user = request.user
    banquinho = str(user)
    objeto_saida = BlocoSaidaModel.objetos.using(banquinho).last()
    n_objeto_saida = BlocoSaidaModel.objetos.using(banquinho).filter(SeBlocoAtual='1').count()
    #n_objeto_saida = objeto_saida.id
    objeto_bloco = model_name.objetos.using(banquinho).get(pk=n_objeto_saida)
    objeto_saida.Dia = str(datetime.date.today())
    objeto_saida.NomeBloco = objeto_bloco.NomeBloco
    objeto_saida.Ordem = objeto_bloco.Ordem
    objeto_saida.Tentativa = objeto_bloco.Tentativa
    objeto_saida.TipoTentativa = objeto_bloco.TipoTentativa
    objeto_saida.Modelo = objeto_bloco.Modelo
    objeto_saida.SupEsq = objeto_bloco.SupEsq
    objeto_saida.SupDir = objeto_bloco.SupDir
    objeto_saida.InfEsq = objeto_bloco.InfEsq
    objeto_saida.InfDir = objeto_bloco.InfDir
    objeto_saida.Reforco = objeto_bloco.Reforco
    objeto_saida.Correta = objeto_bloco.Correta
    objeto_saida.Horario = datetime.datetime.now().strftime('%H:%M:%S')
    objeto_saida.save()

    numero_modelo= numero + 1
    #objeto_bloco = Cond1Bloco01Model.objetos.get(pk=numero_modelo)
    objeto_saida2 = BlocoSaidaModel.objetos.using(banquinho).last()
    objeto_SeAcertou = objeto_saida2.Acertou
    print('o objeto acertou é:', objeto_SeAcertou)
    # -------ultima_tentativa():
    n_saida_ultimo = objeto_saida2.id

    objeto_bloco_ultimo = model_name.objetos.using(banquinho).last()
    n_bloco_ultimo = objeto_bloco_ultimo.id
    print('o  n_bloco_ultimo deu:',  n_bloco_ultimo)
    se_reforco= objeto_bloco.Reforco
    print('se_reforco é:', se_reforco)
    if n_saida_ultimo == n_bloco_ultimo:
        print('acabou!')
        if objeto_SeAcertou == '1':
            return redirect('url_FimBlocoAcertou')
        else:
            return redirect('url_FimBlocoErrou')
    if se_reforco == '0':
        print('sem reforço, irmão')
        return redirect('url_CarregarModelo', pk=numero_modelo)
    else:
        if objeto_SeAcertou == '1':
            return redirect('url_CarregarModeloAcertou', pk=numero_modelo)
        else:
            return redirect('url_CarregarModeloErrou', pk=numero_modelo)
    #template = loader.get_template('MtsApp/CarregarModelo.html')
    #return HttpResponse(template.render(context, request))
    #return redirect('url_CarregarModelo', pk=numero_modelo)

def supdir_view(request):
    user = request.user
    banquinho = str(user)
    objeto_saida = BlocoSaidaModel.objetos.using(banquinho).last()
    ContadorRegistrosAtuais = BlocoSaidaModel.objetos.using(banquinho).filter(SeBlocoAtual='1').count()
    numero = ContadorRegistrosAtuais
    # objeto_saida_ultimo = BlocoSaidaModel.objetos.using(banquinho).last()
    objeto_saida.Escolheu = '2'
    objeto_saida.save()

    # ---SeAcertou-----------------------
    user = request.user
    banquinho = str(user)
    objeto_saida = BlocoSaidaModel.objetos.using(banquinho).last()

    # localizar bloco
    objeto_participante = ParticipanteModel.objetos.using(banquinho).get(pk=1)
    nqualbloco = objeto_participante.NoBlocoProximo
    objeto_TodosOsBlocos = TodosOsBlocos.objetos.using(banquinho).get(NoBloco=nqualbloco)
    xqualbloco = objeto_TodosOsBlocos.NomeBloco
    print('Se deu certo, pegamos o bloco:', xqualbloco)
    model_name = apps.get_model("MtsApp", xqualbloco)
    objeto_bloco = model_name.objetos.using(banquinho).get(pk=1)

    objeto_bloco_ultimo = model_name.objetos.using(banquinho).last()
    total = objeto_bloco_ultimo.id
    n_objeto_saida = BlocoSaidaModel.objetos.using(banquinho).filter(SeBlocoAtual='1').count()
    #n_objeto_saida = objeto_saida.id
    objeto_bloco = model_name.objetos.using(banquinho).get(pk=n_objeto_saida)

    if objeto_bloco.Correta == objeto_saida.Escolheu:
        objeto_saida.Acertou = '1'
        print('parece que acertou')
        # SomAcertou = open('acertou.mp3',"rb")
        # SomAcertou.read()
        # SomAcertou = open('/static/MtsApp/sons/acertou2.wav')
        XCorretas = objeto_saida.Corretas
        NCorretas = int(XCorretas)
        NCorretas += 1
        objeto_saida.Corretas = str(NCorretas)

        Porcent = int(NCorretas * 100 / total)
        objeto_saida.Porcentagem = str(Porcent)
        objeto_saida.ErroTipo = ''
        objeto_saida.save()
    else:
        objeto_saida.Acertou = '0'
        if objeto_bloco.TipoTentativa == "tipo1":
            objeto_saida.ErroTipo = 'errotipo1'
            objeto_saida.save()
        elif objeto_bloco.TipoTentativa == "tipo2":
            objeto_saida.ErroTipo = 'errotipo2'
            objeto_saida.save()
        elif objeto_bloco.TipoTentativa == "tipo3":
            objeto_saida.ErroTipo = 'errotipo3'
            objeto_saida.save()
        objeto_saida.save()

    # ----gravar_saida
    user = request.user
    banquinho = str(user)
    objeto_saida = BlocoSaidaModel.objetos.using(banquinho).last()
    n_objeto_saida= BlocoSaidaModel.objetos.using(banquinho).filter(SeBlocoAtual='1').count()
    #n_objeto_saida = objeto_saida.id

    objeto_bloco = model_name.objetos.using(banquinho).get(pk=n_objeto_saida)
    objeto_saida.Dia = str(datetime.date.today())
    objeto_saida.NomeBloco = objeto_bloco.NomeBloco
    objeto_saida.Ordem = objeto_bloco.Ordem
    objeto_saida.Tentativa = objeto_bloco.Tentativa
    objeto_saida.TipoTentativa = objeto_bloco.TipoTentativa
    objeto_saida.Modelo = objeto_bloco.Modelo
    objeto_saida.SupEsq = objeto_bloco.SupEsq
    objeto_saida.SupDir = objeto_bloco.SupDir
    objeto_saida.InfEsq = objeto_bloco.InfEsq
    objeto_saida.InfDir = objeto_bloco.InfDir
    objeto_saida.Reforco = objeto_bloco.Reforco
    objeto_saida.Correta = objeto_bloco.Correta
    objeto_saida.Horario = datetime.datetime.now().strftime('%H:%M:%S')
    objeto_saida.save()

    numero_modelo = numero + 1
    # objeto_bloco = Cond1Bloco01Model.objetos.get(pk=numero_modelo)
    objeto_saida2 = BlocoSaidaModel.objetos.using(banquinho).last()
    objeto_SeAcertou = objeto_saida2.Acertou
    print('o objeto acertou é:', objeto_SeAcertou)
    # -------ultima_tentativa():
    n_saida_ultimo = objeto_saida2.id

    objeto_bloco_ultimo = model_name.objetos.using(banquinho).last()
    n_bloco_ultimo = objeto_bloco_ultimo.id
    print('o  n_bloco_ultimo deu:', n_bloco_ultimo)
    se_reforco = objeto_bloco.Reforco
    print('se_reforco é:', se_reforco)
    if n_saida_ultimo == n_bloco_ultimo:
        print('acabou!')
        if objeto_SeAcertou == '1':
            return redirect('url_FimBlocoAcertou')
        else:
            return redirect('url_FimBlocoErrou')
    if se_reforco == '0':
        print('sem reforço, irmão')
        return redirect('url_CarregarModelo', pk=numero_modelo)
    else:
        if objeto_SeAcertou == '1':
            return redirect('url_CarregarModeloAcertou', pk=numero_modelo)
        else:
            return redirect('url_CarregarModeloErrou', pk=numero_modelo)
    # template = loader.get_template('MtsApp/CarregarModelo.html')
    # return HttpResponse(template.render(context, request))
    # return redirect('url_CarregarModelo', pk=numero_modelo)

def infesq_view(request):
    user = request.user
    banquinho = str(user)
    objeto_saida = BlocoSaidaModel.objetos.using(banquinho).last()
    ContadorRegistrosAtuais = BlocoSaidaModel.objetos.using(banquinho).filter(SeBlocoAtual='1').count()
    numero = ContadorRegistrosAtuais
    # objeto_saida_ultimo = BlocoSaidaModel.objetos.using(banquinho).last()
    objeto_saida.Escolheu = '3'
    objeto_saida.save()

    # ---SeAcertou-----------------------
    user = request.user
    banquinho = str(user)
    objeto_saida = BlocoSaidaModel.objetos.using(banquinho).last()

    # localizar bloco
    objeto_participante = ParticipanteModel.objetos.using(banquinho).get(pk=1)
    nqualbloco = objeto_participante.NoBlocoProximo
    objeto_TodosOsBlocos = TodosOsBlocos.objetos.using(banquinho).get(NoBloco=nqualbloco)
    xqualbloco = objeto_TodosOsBlocos.NomeBloco
    print('Se deu certo, pegamos o bloco:', xqualbloco)
    model_name = apps.get_model("MtsApp", xqualbloco)
    objeto_bloco = model_name.objetos.using(banquinho).get(pk=1)

    objeto_bloco_ultimo = model_name.objetos.using(banquinho).last()
    total = objeto_bloco_ultimo.id
    n_objeto_saida = BlocoSaidaModel.objetos.using(banquinho).filter(SeBlocoAtual='1').count()
    #n_objeto_saida = objeto_saida.id
    objeto_bloco = model_name.objetos.using(banquinho).get(pk=n_objeto_saida)

    if objeto_bloco.Correta == objeto_saida.Escolheu:
        objeto_saida.Acertou = '1'
        print('parece que acertou')
        # SomAcertou = open('acertou.mp3',"rb")
        # SomAcertou.read()
        # SomAcertou = open('/static/MtsApp/sons/acertou2.wav')
        XCorretas = objeto_saida.Corretas
        NCorretas = int(XCorretas)
        NCorretas += 1
        objeto_saida.Corretas = str(NCorretas)

        Porcent = int(NCorretas * 100 / total)
        objeto_saida.Porcentagem = str(Porcent)
        objeto_saida.ErroTipo = ''
        objeto_saida.save()
    else:
        objeto_saida.Acertou = '0'
        if objeto_bloco.TipoTentativa == "tipo1":
            objeto_saida.ErroTipo = 'errotipo1'
            objeto_saida.save()
        elif objeto_bloco.TipoTentativa == "tipo2":
            objeto_saida.ErroTipo = 'errotipo2'
            objeto_saida.save()
        elif objeto_bloco.TipoTentativa == "tipo3":
            objeto_saida.ErroTipo = 'errotipo3'
            objeto_saida.save()
        objeto_saida.save()

    # ----gravar_saida
    user = request.user
    banquinho = str(user)
    objeto_saida = BlocoSaidaModel.objetos.using(banquinho).last()
    n_objeto_saida = BlocoSaidaModel.objetos.using(banquinho).filter(SeBlocoAtual='1').count()
    #n_objeto_saida = objeto_saida.id

    objeto_bloco = model_name.objetos.using(banquinho).get(pk=n_objeto_saida)
    objeto_saida.Dia = str(datetime.date.today())
    objeto_saida.NomeBloco = objeto_bloco.NomeBloco
    objeto_saida.Ordem = objeto_bloco.Ordem
    objeto_saida.Tentativa = objeto_bloco.Tentativa
    objeto_saida.TipoTentativa = objeto_bloco.TipoTentativa
    objeto_saida.Modelo = objeto_bloco.Modelo
    objeto_saida.SupEsq = objeto_bloco.SupEsq
    objeto_saida.SupDir = objeto_bloco.SupDir
    objeto_saida.InfEsq = objeto_bloco.InfEsq
    objeto_saida.InfDir = objeto_bloco.InfDir
    objeto_saida.Reforco = objeto_bloco.Reforco
    objeto_saida.Correta = objeto_bloco.Correta
    objeto_saida.Horario = datetime.datetime.now().strftime('%H:%M:%S')
    objeto_saida.save()

    numero_modelo = numero + 1
    # objeto_bloco = Cond1Bloco01Model.objetos.get(pk=numero_modelo)
    objeto_saida2 = BlocoSaidaModel.objetos.using(banquinho).last()
    objeto_SeAcertou = objeto_saida2.Acertou
    print('o objeto acertou é:', objeto_SeAcertou)
    # -------ultima_tentativa():
    n_saida_ultimo = objeto_saida2.id

    objeto_bloco_ultimo = model_name.objetos.using(banquinho).last()
    n_bloco_ultimo = objeto_bloco_ultimo.id
    print('o  n_bloco_ultimo deu:', n_bloco_ultimo)
    se_reforco = objeto_bloco.Reforco
    print('se_reforco é:', se_reforco)
    if n_saida_ultimo == n_bloco_ultimo:
        print('acabou!')
        if objeto_SeAcertou == '1':
            return redirect('url_FimBlocoAcertou')
        else:
            return redirect('url_FimBlocoErrou')
    if se_reforco == '0':
        print('sem reforço, irmão')
        return redirect('url_CarregarModelo', pk=numero_modelo)
    else:
        if objeto_SeAcertou == '1':
            return redirect('url_CarregarModeloAcertou', pk=numero_modelo)
        else:
            return redirect('url_CarregarModeloErrou', pk=numero_modelo)
    # template = loader.get_template('MtsApp/CarregarModelo.html')
    # return HttpResponse(template.render(context, request))
    # return redirect('url_CarregarModelo', pk=numero_modelo)

def infdir_view(request):
    user = request.user
    banquinho = str(user)
    objeto_saida = BlocoSaidaModel.objetos.using(banquinho).last()
    ContadorRegistrosAtuais = BlocoSaidaModel.objetos.using(banquinho).filter(SeBlocoAtual='1').count()
    numero = ContadorRegistrosAtuais
    # objeto_saida_ultimo = BlocoSaidaModel.objetos.using(banquinho).last()
    objeto_saida.Escolheu = '4'
    objeto_saida.save()

    # ---SeAcertou-----------------------
    user = request.user
    banquinho = str(user)
    objeto_saida = BlocoSaidaModel.objetos.using(banquinho).last()

    # localizar bloco
    objeto_participante = ParticipanteModel.objetos.using(banquinho).get(pk=1)
    nqualbloco = objeto_participante.NoBlocoProximo
    objeto_TodosOsBlocos = TodosOsBlocos.objetos.using(banquinho).get(NoBloco=nqualbloco)
    xqualbloco = objeto_TodosOsBlocos.NomeBloco
    print('Se deu certo, pegamos o bloco:', xqualbloco)
    model_name = apps.get_model("MtsApp", xqualbloco)
    objeto_bloco = model_name.objetos.using(banquinho).get(pk=1)

    objeto_bloco_ultimo = model_name.objetos.using(banquinho).last()
    total = objeto_bloco_ultimo.id
    n_objeto_saida = BlocoSaidaModel.objetos.using(banquinho).filter(SeBlocoAtual='1').count()
    #n_objeto_saida = objeto_saida.id
    objeto_bloco = model_name.objetos.using(banquinho).get(pk=n_objeto_saida)

    if objeto_bloco.Correta == objeto_saida.Escolheu:
        objeto_saida.Acertou = '1'
        print('parece que acertou')
        # SomAcertou = open('acertou.mp3',"rb")
        # SomAcertou.read()
        # SomAcertou = open('/static/MtsApp/sons/acertou2.wav')
        XCorretas = objeto_saida.Corretas
        NCorretas = int(XCorretas)
        NCorretas += 1
        objeto_saida.Corretas = str(NCorretas)

        Porcent = int(NCorretas * 100 / total)
        objeto_saida.Porcentagem = str(Porcent)
        objeto_saida.ErroTipo = ''
        objeto_saida.save()
    else:
        objeto_saida.Acertou = '0'
        if objeto_bloco.TipoTentativa == "tipo1":
            objeto_saida.ErroTipo = 'errotipo1'
            objeto_saida.save()
        elif objeto_bloco.TipoTentativa == "tipo2":
            objeto_saida.ErroTipo = 'errotipo2'
            objeto_saida.save()
        elif objeto_bloco.TipoTentativa == "tipo3":
            objeto_saida.ErroTipo = 'errotipo3'
            objeto_saida.save()
        objeto_saida.save()

    # ----gravar_saida
    user = request.user
    banquinho = str(user)
    objeto_saida = BlocoSaidaModel.objetos.using(banquinho).last()
    n_objeto_saida = BlocoSaidaModel.objetos.using(banquinho).filter(SeBlocoAtual='1').count()
    #n_objeto_saida = objeto_saida.id

    objeto_bloco = model_name.objetos.using(banquinho).get(pk=n_objeto_saida)
    objeto_saida.Dia = str(datetime.date.today())
    objeto_saida.NomeBloco = objeto_bloco.NomeBloco
    objeto_saida.Ordem = objeto_bloco.Ordem
    objeto_saida.Tentativa = objeto_bloco.Tentativa
    objeto_saida.TipoTentativa = objeto_bloco.TipoTentativa
    objeto_saida.Modelo = objeto_bloco.Modelo
    objeto_saida.SupEsq = objeto_bloco.SupEsq
    objeto_saida.SupDir = objeto_bloco.SupDir
    objeto_saida.InfEsq = objeto_bloco.InfEsq
    objeto_saida.InfDir = objeto_bloco.InfDir
    objeto_saida.Reforco = objeto_bloco.Reforco
    objeto_saida.Correta = objeto_bloco.Correta
    objeto_saida.Horario = datetime.datetime.now().strftime('%H:%M:%S')
    objeto_saida.save()

    numero_modelo = numero + 1
    # objeto_bloco = Cond1Bloco01Model.objetos.get(pk=numero_modelo)
    objeto_saida2 = BlocoSaidaModel.objetos.using(banquinho).last()
    objeto_SeAcertou = objeto_saida2.Acertou
    print('o objeto acertou é:', objeto_SeAcertou)
    # -------ultima_tentativa():
    n_saida_ultimo = objeto_saida2.id

    objeto_bloco_ultimo = model_name.objetos.using(banquinho).last()
    n_bloco_ultimo = objeto_bloco_ultimo.id
    print('o  n_bloco_ultimo deu:', n_bloco_ultimo)
    se_reforco = objeto_bloco.Reforco
    print('se_reforco é:', se_reforco)
    if n_saida_ultimo == n_bloco_ultimo:
        print('acabou!')
        if objeto_SeAcertou == '1':
            return redirect('url_FimBlocoAcertou')
        else:
            return redirect('url_FimBlocoErrou')
    if se_reforco == '0':
        print('sem reforço, irmão')
        return redirect('url_CarregarModelo', pk=numero_modelo)
    else:
        if objeto_SeAcertou == '1':
            return redirect('url_CarregarModeloAcertou', pk=numero_modelo)
        else:
            return redirect('url_CarregarModeloErrou', pk=numero_modelo)
    # template = loader.get_template('MtsApp/CarregarModelo.html')
    # return HttpResponse(template.render(context, request))
    # return redirect('url_CarregarModelo', pk=numero_modelo)

def CarregarModelo_view(request, pk):
    # -------ultima_tentativa():
    user = request.user
    banquinho = str(user)
    objeto_saida = BlocoSaidaModel.objetos.using(banquinho).last()
    n_saida_ultimo = BlocoSaidaModel.objetos.using(banquinho).filter(SeBlocoAtual='1').count()
    #n_saida_ultimo = objeto_saida.id

    # localizar bloco
    objeto_participante = ParticipanteModel.objetos.using(banquinho).get(pk=1)
    nqualbloco = objeto_participante.NoBlocoProximo
    objeto_TodosOsBlocos = TodosOsBlocos.objetos.using(banquinho).get(NoBloco=nqualbloco)
    xqualbloco = objeto_TodosOsBlocos.NomeBloco
    print('Se deu certo, pegamos o bloco:', xqualbloco)
    model_name = apps.get_model("MtsApp", xqualbloco)

    objeto_bloco_ultimo = model_name.objetos.using(banquinho).last()
    n_bloco_ultimo = objeto_bloco_ultimo.id
    if n_saida_ultimo == n_bloco_ultimo:
        print('acabou!')
        return redirect('url_FimBloco')

    #objeto_saida = BlocoSaidaModel.objetos.using(banquinho).last()
    objeto_bloco = model_name.objetos.using(banquinho).get(pk=pk)
    ContadorRegistrosAtuais = BlocoSaidaModel.objetos.using(banquinho).filter(SeBlocoAtual='1').count()
    numero = ContadorRegistrosAtuais
    numero = numero + 1
    user = request.user
    banquinho = str(user)
    objeto_saida = BlocoSaidaModel.objetos.using(banquinho).last()
    n_saida_ultimo = objeto_saida.id
    pk_next = n_saida_ultimo + 1
    objeto_saida.pk = None
    objeto_saida.pk = pk_next
    objeto_saida.save()
    # -------gravar saida default
    objeto_saida.Acertou = '0'
    objeto_saida.save()
    print('novo pk_next, com inserir_registro_saida', pk_next)

    form = BlocoSaidaForm(request.POST or None, instance=objeto_bloco)
    context= {
        'objeto_bloco': objeto_bloco,
        #'objeto_saida': objeto_saida,
        'numero': numero,
        'form': form,
    }
    template = loader.get_template('MtsApp/CarregarModelo.html')
    return HttpResponse(template.render(context, request))
    #return render(request, 'MtsApp/CarregarModelo.html', context)

def CarregarModeloAcertou_view(request, pk):
    # -------ultima_tentativa():
    user = request.user
    banquinho = str(user)
    objeto_saida = BlocoSaidaModel.objetos.using(banquinho).last()
    n_saida_ultimo = BlocoSaidaModel.objetos.using(banquinho).filter(SeBlocoAtual='1').count()
    #n_saida_ultimo = objeto_saida.id

    # localizar bloco
    objeto_participante = ParticipanteModel.objetos.using(banquinho).get(pk=1)
    nqualbloco = objeto_participante.NoBlocoProximo
    objeto_TodosOsBlocos = TodosOsBlocos.objetos.using(banquinho).get(NoBloco=nqualbloco)
    xqualbloco = objeto_TodosOsBlocos.NomeBloco
    print('Se deu certo, pegamos o bloco:', xqualbloco)
    model_name = apps.get_model("MtsApp", xqualbloco)
    #objeto_bloco = model_name.objetos.using(banquinho).get(pk=1)

    objeto_bloco_ultimo = model_name.objetos.using(banquinho).last()
    n_bloco_ultimo = objeto_bloco_ultimo.id
    print('rodando o SeUltimo', 'n_bloco_ultimo: ', n_bloco_ultimo, 'n_saida_ultimo: ', n_saida_ultimo)
    if n_saida_ultimo == n_bloco_ultimo:
        print('acabou!')
        return redirect('url_FimBloco')

    objeto_saida = BlocoSaidaModel.objetos.using(banquinho).last()
    objeto_bloco = model_name.objetos.using(banquinho).get(pk=pk)
    ContadorRegistrosAtuais = BlocoSaidaModel.objetos.using(banquinho).filter(SeBlocoAtual='1').count()
    numero = ContadorRegistrosAtuais
    numero = numero + 1
    user = request.user
    banquinho = str(user)
    objeto_saida = BlocoSaidaModel.objetos.using(banquinho).last()
    n_saida_ultimo = objeto_saida.id
    pk_next = n_saida_ultimo + 1
    objeto_saida.pk = None
    objeto_saida.pk = pk_next
    objeto_saida.save()
    # -------gravar saida default
    objeto_saida.Acertou = '0'
    objeto_saida.save()
    print('novo pk_next, com inserir_registro_saida', pk_next)


    form = BlocoSaidaForm(request.POST or None, instance=objeto_bloco)
    context= {
        'objeto_bloco': objeto_bloco,
        #'objeto_saida': objeto_saida,
        'numero': numero,
        'form': form,
    }
    template = loader.get_template('MtsApp/CarregarModeloAcertou.html')
    return HttpResponse(template.render(context, request))
    #return render(request, 'MtsApp/CarregarModelo.html', context)

def CarregarModeloErrou_view(request, pk):
    # -------ultima_tentativa():
    user = request.user
    banquinho = str(user)
    objeto_saida = BlocoSaidaModel.objetos.using(banquinho).last()
    n_saida_ultimo = BlocoSaidaModel.objetos.using(banquinho).filter(SeBlocoAtual='1').count()
    #n_saida_ultimo = objeto_saida.id

    # localizar bloco
    objeto_participante = ParticipanteModel.objetos.using(banquinho).get(pk=1)
    nqualbloco = objeto_participante.NoBlocoProximo
    objeto_TodosOsBlocos = TodosOsBlocos.objetos.using(banquinho).get(NoBloco=nqualbloco)
    xqualbloco = objeto_TodosOsBlocos.NomeBloco
    print('Se deu certo, pegamos o bloco:', xqualbloco)
    model_name = apps.get_model("MtsApp", xqualbloco)
    #objeto_bloco = model_name.objetos.using(banquinho).get(pk=1)

    objeto_bloco_ultimo = model_name.objetos.using(banquinho).last()
    n_bloco_ultimo = objeto_bloco_ultimo.id
    print('rodando o SeUltimo', 'n_bloco_ultimo: ', n_bloco_ultimo, 'n_saida_ultimo: ', n_saida_ultimo)
    if n_saida_ultimo == n_bloco_ultimo:
        print('acabou!')
        return redirect('url_FimBloco')

    objeto_saida = BlocoSaidaModel.objetos.using(banquinho).last()
    objeto_bloco = model_name.objetos.using(banquinho).get(pk=pk)
    ContadorRegistrosAtuais = BlocoSaidaModel.objetos.using(banquinho).filter(SeBlocoAtual='1').count()
    numero = ContadorRegistrosAtuais
    numero = numero + 1
    user = request.user
    banquinho = str(user)
    objeto_saida = BlocoSaidaModel.objetos.using(banquinho).last()
    n_saida_ultimo = objeto_saida.id
    pk_next = n_saida_ultimo + 1
    objeto_saida.pk = None
    objeto_saida.pk = pk_next
    objeto_saida.save()
    # -------gravar saida default
    objeto_saida.Acertou = '0'
    objeto_saida.save()
    print('novo pk_next, com inserir_registro_saida', pk_next)


    form = BlocoSaidaForm(request.POST or None, instance=objeto_bloco)
    context= {
        'objeto_bloco': objeto_bloco,
        #'objeto_saida': objeto_saida,
        'numero': numero,
        'form': form,
    }
    template = loader.get_template('MtsApp/CarregarModeloErrou.html')
    return HttpResponse(template.render(context, request))
    #return render(request, 'MtsApp/CarregarModelo.html', context)


def CarregarComparacoes_view(request, pk):
    user = request.user
    banquinho = str(user)
    objeto_saida = BlocoSaidaModel.objetos.using(banquinho).get(pk=pk)
    ContadorRegistrosAtuais = BlocoSaidaModel.objetos.using(banquinho).filter(SeBlocoAtual='1').count()
    numero = ContadorRegistrosAtuais
    #numero = objeto_saida.id

    # localizar bloco
    objeto_participante = ParticipanteModel.objetos.using(banquinho).get(pk=1)
    nqualbloco = objeto_participante.NoBlocoProximo
    objeto_TodosOsBlocos = TodosOsBlocos.objetos.using(banquinho).get(NoBloco=nqualbloco)
    xqualbloco = objeto_TodosOsBlocos.NomeBloco
    print('Se deu certo, pegamos o bloco:', xqualbloco)
    model_name = apps.get_model("MtsApp", xqualbloco)
    #objeto_bloco = model_name.objetos.using(banquinho).get(pk=1)

    objeto_bloco= model_name.objetos.using(banquinho).get(pk=numero)
    # ------

    #objeto_bloco= Cond1Bloco01Model.objetos.using(banquinho).get(pk=numero)
    form = BlocoSaidaForm(request.POST or None, instance=objeto_saida)
    context = {
       'objeto_bloco': objeto_bloco,
       'objeto_saida': objeto_saida,
       'numero': numero,
       'form': form,
    }
    template = loader.get_template('MtsApp/CarregarComparacoes.html')
    return HttpResponse(template.render(context, request))
    #return render(request, 'MtsApp/CarregarComparacoes.html', context)

def FimBloco_view(request):

    if request.POST.get('voltar'):
        user = request.user
        banquinho = str(user)
        objeto_saida = BlocoSaidaModel.objetos.using(banquinho).last()

        # Verificar critérios
        nErrosTipo1 = BlocoSaidaModel.objetos.using(banquinho).filter(ErroTipo='errotipo1', SeBlocoAtual='1').count()
        nErrosTipo2 = BlocoSaidaModel.objetos.using(banquinho).filter(ErroTipo='errotipo2', SeBlocoAtual='1').count()
        nErrosTipo3 = BlocoSaidaModel.objetos.using(banquinho).filter(ErroTipo='errotipo3', SeBlocoAtual='1').count()
        nPorcent = objeto_saida.Porcentagem
        print('A porcentagem de acertos foi:', nPorcent)
        print('Para tentativa do tipo 1, errou tantas vezes:', nErrosTipo1)
        print('Para tentativa do tipo 2, errou tantas vezes:', nErrosTipo2)
        print('Para tentativa do tipo 3, errou tantas vezes:', nErrosTipo3)
        xcriterioporcent = 'SIM'
        xcriteriotent = 'SIM'
        xpassou = 'NAO'
        if nErrosTipo1 > 2: xcriteriotent = 'NAO'
        if nErrosTipo2 > 2: xcriteriotent = 'NAO'
        if nErrosTipo3 > 2: xcriteriotent = 'NAO'
        if int(nPorcent) < 90: xcriterioporcent = 'NAO'
        print('E aí? Atingiu o critério de porcentagem? ', xcriterioporcent)
        print('E aí? Atingiu o critério de tentativas? ', xcriteriotent)
        if xcriterioporcent == 'SIM' and xcriteriotent == 'SIM':
            xpassou = 'SIM'
        print('Passou adiante?', xpassou)

        # Gravar próximo bloco
        objeto_participante = ParticipanteModel.objetos.using(banquinho).get(pk=1)
        nqualbloco = objeto_participante.NoBlocoProximo
        objeto_TodosOsBlocos = TodosOsBlocos.objetos.using(banquinho).get(NoBloco=nqualbloco)
        nCriterioSim = objeto_TodosOsBlocos.CriterioSim
        nCriterioNao = objeto_TodosOsBlocos.CriterioNao

        if xpassou == 'SIM':
            objeto_participante.NoBlocoProximo = nCriterioSim
            objeto_participante.save()
            print('linha 950, passou; objeto_participante.NoBlocoProximo: ', nCriterioSim)
        else:
            objeto_participante.NoBlocoProximo = nCriterioNao
            objeto_participante.save()
            print('Linha 954, não passou; objeto_participante.NoBlocoProximo: ', nCriterioNao)
        return redirect('url_Entrada_Iniciar')

    if request.POST.get('proximo'):
        user = request.user
        banquinho = str(user)
        objeto_saida = BlocoSaidaModel.objetos.using(banquinho).last()

        # Verificar critérios
        nErrosTipo1 = BlocoSaidaModel.objetos.using(banquinho).filter(ErroTipo='errotipo1', SeBlocoAtual='1').count()
        nErrosTipo2 = BlocoSaidaModel.objetos.using(banquinho).filter(ErroTipo='errotipo2', SeBlocoAtual='1').count()
        nErrosTipo3 = BlocoSaidaModel.objetos.using(banquinho).filter(ErroTipo='errotipo3', SeBlocoAtual='1').count()
        nPorcent = objeto_saida.Porcentagem
        print('A porcentagem de acertos foi:', nPorcent)
        print('Para tentativa do tipo 1, errou tantas vezes:', nErrosTipo1)
        print('Para tentativa do tipo 2, errou tantas vezes:', nErrosTipo2)
        print('Para tentativa do tipo 3, errou tantas vezes:', nErrosTipo3)
        xcriterioporcent = 'SIM'
        xcriteriotent = 'SIM'
        xpassou = 'NAO'
        if nErrosTipo1 > 2: xcriteriotent = 'NAO'
        if nErrosTipo2 > 2: xcriteriotent = 'NAO'
        if nErrosTipo3 > 2: xcriteriotent = 'NAO'
        if int(nPorcent) < 90: xcriterioporcent = 'NAO'
        print('E aí? Atingiu o critério de porcentagem? ', xcriterioporcent)
        print('E aí? Atingiu o critério de tentativas? ', xcriteriotent)
        if xcriterioporcent == 'SIM' and xcriteriotent == 'SIM':
            xpassou = 'SIM'
        print('Passou adiante?', xpassou)

        # Gravar próximo bloco
        objeto_participante = ParticipanteModel.objetos.using(banquinho).get(pk=1)
        nqualbloco = objeto_participante.NoBlocoProximo
        objeto_TodosOsBlocos = TodosOsBlocos.objetos.using(banquinho).get(NoBloco=nqualbloco)
        nCriterioSim = objeto_TodosOsBlocos.CriterioSim
        nCriterioNao = objeto_TodosOsBlocos.CriterioNao

        if xpassou == 'SIM':
            objeto_participante.NoBlocoProximo = nCriterioSim
            objeto_participante.save()
            print('linha 950, passou; objeto_participante.NoBlocoProximo: ', nCriterioSim)
        else:
            objeto_participante.NoBlocoProximo = nCriterioNao
            objeto_participante.save()
            print('Linha 954, não passou; objeto_participante.NoBlocoProximo: ', nCriterioNao)
        return redirect('url_Comecar_bloco')

    return render(request, 'MtsApp/FimBloco.html')

def FimBlocoAcertou_view(request):

    if request.POST.get('voltar'):
        user = request.user
        banquinho = str(user)
        objeto_saida = BlocoSaidaModel.objetos.using(banquinho).last()

        # Verificar critérios
        nErrosTipo1 = BlocoSaidaModel.objetos.using(banquinho).filter(ErroTipo='errotipo1', SeBlocoAtual='1').count()
        nErrosTipo2 = BlocoSaidaModel.objetos.using(banquinho).filter(ErroTipo='errotipo2', SeBlocoAtual='1').count()
        nErrosTipo3 = BlocoSaidaModel.objetos.using(banquinho).filter(ErroTipo='errotipo3', SeBlocoAtual='1').count()
        nPorcent = objeto_saida.Porcentagem
        print('A porcentagem de acertos foi:', nPorcent)
        print('Para tentativa do tipo 1, errou tantas vezes:', nErrosTipo1)
        print('Para tentativa do tipo 2, errou tantas vezes:', nErrosTipo2)
        print('Para tentativa do tipo 3, errou tantas vezes:', nErrosTipo3)
        xcriterioporcent = 'SIM'
        xcriteriotent = 'SIM'
        xpassou = 'NAO'
        if nErrosTipo1 > 2: xcriteriotent = 'NAO'
        if nErrosTipo2 > 2: xcriteriotent = 'NAO'
        if nErrosTipo3 > 2: xcriteriotent = 'NAO'
        if int(nPorcent) < 90: xcriterioporcent = 'NAO'
        print('E aí? Atingiu o critério de porcentagem? ', xcriterioporcent)
        print('E aí? Atingiu o critério de tentativas? ', xcriteriotent)
        if xcriterioporcent == 'SIM' and xcriteriotent == 'SIM':
            xpassou = 'SIM'
        print('Passou adiante?', xpassou)

        # Gravar próximo bloco
        objeto_participante = ParticipanteModel.objetos.using(banquinho).get(pk=1)
        nqualbloco = objeto_participante.NoBlocoProximo
        objeto_TodosOsBlocos = TodosOsBlocos.objetos.using(banquinho).get(NoBloco=nqualbloco)
        nCriterioSim = objeto_TodosOsBlocos.CriterioSim
        nCriterioNao = objeto_TodosOsBlocos.CriterioNao

        if xpassou == 'SIM':
            objeto_participante.NoBlocoProximo = nCriterioSim
            objeto_participante.save()
            print('linha 950, passou; objeto_participante.NoBlocoProximo: ', nCriterioSim)
        else:
            objeto_participante.NoBlocoProximo = nCriterioNao
            objeto_participante.save()
            print('Linha 954, não passou; objeto_participante.NoBlocoProximo: ', nCriterioNao)
        return redirect('url_Entrada_Iniciar')

    if request.POST.get('proximo'):
        user = request.user
        banquinho = str(user)
        objeto_saida = BlocoSaidaModel.objetos.using(banquinho).last()

        # Verificar critérios
        nErrosTipo1 = BlocoSaidaModel.objetos.using(banquinho).filter(ErroTipo='errotipo1', SeBlocoAtual='1').count()
        nErrosTipo2 = BlocoSaidaModel.objetos.using(banquinho).filter(ErroTipo='errotipo2', SeBlocoAtual='1').count()
        nErrosTipo3 = BlocoSaidaModel.objetos.using(banquinho).filter(ErroTipo='errotipo3', SeBlocoAtual='1').count()
        nPorcent = objeto_saida.Porcentagem
        print('A porcentagem de acertos foi:', nPorcent)
        print('Para tentativa do tipo 1, errou tantas vezes:', nErrosTipo1)
        print('Para tentativa do tipo 2, errou tantas vezes:', nErrosTipo2)
        print('Para tentativa do tipo 3, errou tantas vezes:', nErrosTipo3)
        xcriterioporcent = 'SIM'
        xcriteriotent = 'SIM'
        xpassou = 'NAO'
        if nErrosTipo1 > 2: xcriteriotent = 'NAO'
        if nErrosTipo2 > 2: xcriteriotent = 'NAO'
        if nErrosTipo3 > 2: xcriteriotent = 'NAO'
        if int(nPorcent) < 90: xcriterioporcent = 'NAO'
        print('E aí? Atingiu o critério de porcentagem? ', xcriterioporcent)
        print('E aí? Atingiu o critério de tentativas? ', xcriteriotent)
        if xcriterioporcent == 'SIM' and xcriteriotent == 'SIM':
            xpassou = 'SIM'
        print('Passou adiante?', xpassou)

        # Gravar próximo bloco
        objeto_participante = ParticipanteModel.objetos.using(banquinho).get(pk=1)
        nqualbloco = objeto_participante.NoBlocoProximo
        objeto_TodosOsBlocos = TodosOsBlocos.objetos.using(banquinho).get(NoBloco=nqualbloco)
        nCriterioSim = objeto_TodosOsBlocos.CriterioSim
        nCriterioNao = objeto_TodosOsBlocos.CriterioNao

        if xpassou == 'SIM':
            objeto_participante.NoBlocoProximo = nCriterioSim
            objeto_participante.save()
            print('linha 950, passou; objeto_participante.NoBlocoProximo: ', nCriterioSim)
        else:
            objeto_participante.NoBlocoProximo = nCriterioNao
            objeto_participante.save()
            print('Linha 954, não passou; objeto_participante.NoBlocoProximo: ', nCriterioNao)
        return redirect('url_Comecar_bloco')

    return render(request, 'MtsApp/FimBlocoAcertou.html')

def FimBlocoErrou_view(request):

    if request.POST.get('voltar'):
        user = request.user
        banquinho = str(user)
        objeto_saida = BlocoSaidaModel.objetos.using(banquinho).last()

        # Verificar critérios
        nErrosTipo1 = BlocoSaidaModel.objetos.using(banquinho).filter(ErroTipo='errotipo1', SeBlocoAtual='1').count()
        nErrosTipo2 = BlocoSaidaModel.objetos.using(banquinho).filter(ErroTipo='errotipo2', SeBlocoAtual='1').count()
        nErrosTipo3 = BlocoSaidaModel.objetos.using(banquinho).filter(ErroTipo='errotipo3', SeBlocoAtual='1').count()
        nPorcent = objeto_saida.Porcentagem
        print('A porcentagem de acertos foi:', nPorcent)
        print('Para tentativa do tipo 1, errou tantas vezes:', nErrosTipo1)
        print('Para tentativa do tipo 2, errou tantas vezes:', nErrosTipo2)
        print('Para tentativa do tipo 3, errou tantas vezes:', nErrosTipo3)
        xcriterioporcent = 'SIM'
        xcriteriotent = 'SIM'
        xpassou = 'NAO'
        if nErrosTipo1 > 2: xcriteriotent = 'NAO'
        if nErrosTipo2 > 2: xcriteriotent = 'NAO'
        if nErrosTipo3 > 2: xcriteriotent = 'NAO'
        if int(nPorcent) < 90: xcriterioporcent = 'NAO'
        print('E aí? Atingiu o critério de porcentagem? ', xcriterioporcent)
        print('E aí? Atingiu o critério de tentativas? ', xcriteriotent)
        if xcriterioporcent == 'SIM' and xcriteriotent == 'SIM':
            xpassou = 'SIM'
        print('Passou adiante?', xpassou)

        # Gravar próximo bloco
        objeto_participante = ParticipanteModel.objetos.using(banquinho).get(pk=1)
        nqualbloco = objeto_participante.NoBlocoProximo
        objeto_TodosOsBlocos = TodosOsBlocos.objetos.using(banquinho).get(NoBloco=nqualbloco)
        nCriterioSim = objeto_TodosOsBlocos.CriterioSim
        nCriterioNao = objeto_TodosOsBlocos.CriterioNao

        if xpassou == 'SIM':
            objeto_participante.NoBlocoProximo = nCriterioSim
            objeto_participante.save()
            print('linha 950, passou; objeto_participante.NoBlocoProximo: ', nCriterioSim)
        else:
            objeto_participante.NoBlocoProximo = nCriterioNao
            objeto_participante.save()
            print('Linha 954, não passou; objeto_participante.NoBlocoProximo: ', nCriterioNao)
        return redirect('url_Entrada_Iniciar')

    if request.POST.get('proximo'):
        user = request.user
        banquinho = str(user)
        objeto_saida = BlocoSaidaModel.objetos.using(banquinho).last()

        # Verificar critérios
        nErrosTipo1 = BlocoSaidaModel.objetos.using(banquinho).filter(ErroTipo='errotipo1', SeBlocoAtual='1').count()
        nErrosTipo2 = BlocoSaidaModel.objetos.using(banquinho).filter(ErroTipo='errotipo2', SeBlocoAtual='1').count()
        nErrosTipo3 = BlocoSaidaModel.objetos.using(banquinho).filter(ErroTipo='errotipo3', SeBlocoAtual='1').count()
        nPorcent = objeto_saida.Porcentagem
        print('A porcentagem de acertos foi:', nPorcent)
        print('Para tentativa do tipo 1, errou tantas vezes:', nErrosTipo1)
        print('Para tentativa do tipo 2, errou tantas vezes:', nErrosTipo2)
        print('Para tentativa do tipo 3, errou tantas vezes:', nErrosTipo3)
        xcriterioporcent = 'SIM'
        xcriteriotent = 'SIM'
        xpassou = 'NAO'
        if nErrosTipo1 > 2: xcriteriotent = 'NAO'
        if nErrosTipo2 > 2: xcriteriotent = 'NAO'
        if nErrosTipo3 > 2: xcriteriotent = 'NAO'
        if int(nPorcent) < 90: xcriterioporcent = 'NAO'
        print('E aí? Atingiu o critério de porcentagem? ', xcriterioporcent)
        print('E aí? Atingiu o critério de tentativas? ', xcriteriotent)
        if xcriterioporcent == 'SIM' and xcriteriotent == 'SIM':
            xpassou = 'SIM'
        print('Passou adiante?', xpassou)

        # Gravar próximo bloco
        objeto_participante = ParticipanteModel.objetos.using(banquinho).get(pk=1)
        nqualbloco = objeto_participante.NoBlocoProximo
        objeto_TodosOsBlocos = TodosOsBlocos.objetos.using(banquinho).get(NoBloco=nqualbloco)
        nCriterioSim = objeto_TodosOsBlocos.CriterioSim
        nCriterioNao = objeto_TodosOsBlocos.CriterioNao

        if xpassou == 'SIM':
            objeto_participante.NoBlocoProximo = nCriterioSim
            objeto_participante.save()
            print('linha 950, passou; objeto_participante.NoBlocoProximo: ', nCriterioSim)
        else:
            objeto_participante.NoBlocoProximo = nCriterioNao
            objeto_participante.save()
            print('Linha 954, não passou; objeto_participante.NoBlocoProximo: ', nCriterioNao)
        return redirect('url_Comecar_bloco')


    return render(request, 'MtsApp/FimBlocoErrou.html')

"""
@login_required
def comecar_sessao_view(request):
    context = {}
    user = request.user
    banquinho = str(user)
    #objetinho = EprogModel.objetos.using(banquinho).get(pk=pk)
    objetinho_sessao = SessaoModel.objetos.using(banquinho).get(pk=1)
    n_tentativa = objetinho_sessao.NTopico
    objetinho = EprogModel.objetos.using(banquinho).get(pk=n_tentativa)
    form = EprogForm(request.POST or None, instance=objetinho)
    objeto_procedimento = ProcedimentoModel.objetos.get(pk=1)


    if request.POST.get('comecar_sessao'):
        context = {}
        user = request.user
        banquinho = str(user)
        obj = EprogModel.objetos.using(banquinho).last()
        objetinho_sessao = SessaoModel.objetos.using(banquinho).get(pk=1)
        n_tentativa = objetinho_sessao.NTopico
        #data = {}
        #pk = n_tentativa
        objetinho = EprogModel.objetos.using('banquinho').get(pk=n_tentativa)
        form = EprogForm(request.POST or None, instance=objetinho)
        #data['form'] = form
        #data['objetinho'] = objetinho
        context = {
            'objetinho_sessao': objetinho_sessao,
            "form": form,
            "objetinho": objetinho,
            #"objetinho2": objetinho2
        }
        return redirect('url_principal', pk= n_tentativa)
        #return redirect('url_principal', context)
        #return render(request,'url_sessao', context)
        #return render(request, 'EprogApp/sessao.html', data)

    context = {
        "objetinho_sessao": objetinho_sessao,
        "form": form,
        "objetinho": objetinho,
        "n_tentativa": n_tentativa
    }
    return render(request, "MtsApp/comecar_sessao.html", context)

#@login_required
def Entrada_Um(request):
    objeto_saida = BlocoSaidaModel.objetos.get(pk=1)
    form = BlocoSaidaForm(request.POST or None, instance=objeto_saida)
    if request.POST.get('rodar_bloco'):
        return redirect('url_ComecarBloco')

    if request.POST.get('rodar_blocoJS'):
        return redirect('url_BlocoJs')

    if request.POST.get('ResetSaida'):
        ResetSaida()
        print('tudo apagado')
        #return HttpResponse('Tudo apagado')

    context = {
        'objeto_saida': objeto_saida,
        "form": form,
    }
    return render(request, 'MtsApp/EntradaUm.html')

#@login_required
def listagem(request):
    context = {}
    banquinho = 'eprog_p1'
    lista = Cond1Bloco01Model.objetos.all()

    if request.POST.get('rodar_bloco'):
        return redirect('url_comecar_bloco')

    context = {
        'lista': lista,
    }
    return render(request, 'MtsApp/listagem.html', context)

def janelas_teste(request):
    objeto_janela = Cond1Bloco01Model.objetos.get(pk=9)
    if request.POST.get('Embora'):
        return redirect('url_listagem')

    context = {'objeto_janela': objeto_janela}
    return render(request, 'MtsApp/Janelas_teste.html', context)

def janelas(request):
    objeto_janela= Cond1Bloco01Model.objetos.get(pk=8)
    if request.POST.get('Embora'):
        #return HttpResponse("Hello, world. You're at ")
        return redirect('url_listagem')

    if request.POST.get('voltar'):
        objeto_janela = Cond1Bloco01Model.objetos.get(pk=2)
        context = {'objeto_janela': objeto_janela}
        return HttpResponse("Hello, world. You're at ")
        #return render(request, 'MtsApp/Janelas.html', context)
        #return redirect('url_listagem')
        #return render(request, 'MtsApp/listagem.html', context)

    context= {'objeto_janela': objeto_janela}
    return render(request, 'MtsApp/Janelas.html', context)


def modelo_view(request):
    print('Vc apertou o botao do meio')
    return redirect('url_Entrada_Um')
    #return redirect('url_janelas')
   
def ChamaJson(request):
    user = request.user
    banquinho = str(user)
    objeto_bloco = Cond1Bloco01Model.objetos.using(banquinho).get(pk=9)
    objeto_tentativa = objeto_bloco.Tentativa
   #objeto_tentativa_js = list(objeto_tentativa)  # important: convert the QuerySet to a list object
    #return JsonResponse(objeto_tentativa_js, safe=False)

    context = {
        'objeto_bloco': objeto_bloco,
    }
    #return render(request, 'MtsApp/BlocoJs2.html', context)
    template = loader.get_template('MtsApp/BlocoJs2.html')
    return HttpResponse(template.render(context, request))

def ClickE1(request):
    user = request.user
    banquinho = str(user)
    objeto_bloco = Cond1Bloco01Model.objetos.using(banquinho).get(pk=1)
    context = {
        'objeto_bloco': objeto_bloco,
    }
    template = loader.get_template('MtsApp/BlocoJs2.html')
    return HttpResponse(template.render(context, request))

def ClickE2(request):
    user = request.user
    banquinho = str(user)
    objeto_bloco = Cond1Bloco01Model.objetos.using(banquinho).get(pk=8)
    context = {
        'objeto_bloco': objeto_bloco,
    }
    template = loader.get_template('MtsApp/BlocoJs2.html')
    return HttpResponse(template.render(context, request))

def ClickE3(request):
    user = request.user
    banquinho = str(user)
    objeto_bloco = Cond1Bloco01Model.objetos.using(banquinho).get(pk=12)
    context = {
        'objeto_bloco': objeto_bloco,
    }
    template = loader.get_template('MtsApp/BlocoJs2.html')
    return HttpResponse(template.render(context, request))

def ClickDjango(request):
    return HttpResponse("Hello,motherfuckers!")
    #objeto_bloco = Cond1Bloco01Model.objetos.get(pk=9)
    #objeto_tentativa = objeto_bloco.Tentativa
    #print('Pelo menos eu entrei')
    #HttpResponse(objeto_tentativa)    

def BlocoJs_view(request):
    print('Esse é o bloco JS')
    #json_serializer = serializers.get_serializer("json")()
    #Tentativa = json_serializer.serialize(Cond1Bloco01Model.objetos.get(pk=1)('id')[:5], ensure_ascii=False)
    print('Agora executando comecar_bloco_view')
    #json_serializer = serializers.get_serializer("json")()
    #objeto_tentativa_js = json_serializer.serialize(Cond1Bloco01Model.objetos.get(pk=9), ensure_ascii=False)

    #if request.POST.get('BotaoDeFora'):
    #objeto_tentativa = serializers.serialize("json", Cond1Bloco01Model.objetos.get(pk=9))
    #    json_serializer = serializers.get_serializer("json")()
    #    objeto_tentativa_js = json_serializer.serialize(Cond1Bloco01Model.objetos.get(pk=9), ensure_ascii=False)
    #    companies = json_serializer.serialize(Company.objects.all().order_by('id')[:5], ensure_ascii=False)

    if request.POST.get('BotaoDeFora'):
        objeto_blocoJSX = Cond1Bloco01Model.objetos.get(pk=9)
        objeto_tentativa = objeto_blocoJSX.Tentativa
        # objeto_tentativa_js = list(objeto_tentativa)  # important: convert the QuerySet to a list object

        return JsonResponse(objeto_tentativa, safe=False)
        #return JsonResponse({"objeto_tentativa": objeto_tentativa}) # também funciona
        #return HttpResponse(json.dumps(objeto_tentativa), content_type="application/json") # também funciona



    objeto_saida = BlocoSaidaModel.objetos.get(pk=1)
    form = BlocoSaidaForm(request.POST or None, instance=objeto_saida)
    objeto_bloco = Cond1Bloco01Model.objetos.get(pk=1)
    objeto_saida = BlocoSaidaModel.objetos.get(pk=1)
    numero = objeto_saida.id
    # objeto_saida_ultimo = BlocoSaidaModel.objetos.using(banquinho).last()
    objeto_saida.Dia = str(datetime.date.today())
    objeto_saida.NomeBloco = objeto_bloco.NomeBloco
    objeto_saida.Ordem = objeto_bloco.Ordem
    objeto_saida.Tentativa = objeto_bloco.Tentativa
    objeto_saida.Modelo = objeto_bloco.Modelo
    objeto_saida.SupEsq = objeto_bloco.SupEsq
    objeto_saida.SupDir = objeto_bloco.SupDir
    objeto_saida.InfEsq = objeto_bloco.InfEsq
    objeto_saida.InfDir = objeto_bloco.InfDir
    objeto_saida.Reforco = objeto_bloco.Reforco
    objeto_saida.Correta = objeto_bloco.Correta
    objeto_saida.Horario = datetime.datetime.now().strftime('%H:%M:%S')
    objeto_saida.Ordem = '1'
    objeto_saida.save()

    context = {
        'objeto_bloco': objeto_bloco,
        'form': form,
        'numero': numero,
    }
    return render(request, 'MtsApp/BlocoJs2.html', context)

def Js_View():
    objeto_blocoJSX = Cond1Bloco01Model.objetos.get(pk=9)
    objeto_tentativa = objeto_blocoJSX.Tentativa
    return JsonResponse(objeto_tentativa, safe=False)

    #json_serializer = serializers.get_serializer("json")()
    #objeto_tentativa_js = json_serializer.serialize(Cond1Bloco01Model.objetos.get(pk=9), ensure_ascii=False)

    #if request.POST.get('BotaoDeFora'):
    #objeto_tentativa = serializers.serialize("json", Cond1Bloco01Model.objetos.get(pk=9))
    #    json_serializer = serializers.get_serializer("json")()
    #    objeto_tentativa_js = json_serializer.serialize(Cond1Bloco01Model.objetos.get(pk=9), ensure_ascii=False)
    #    companies = json_serializer.serialize(Company.objects.all().order_by('id')[:5], ensure_ascii=False)

    #if request.POST.get('BotaoDeFora'):
        #objeto_blocoJSX = Cond1Bloco01Model.objetos.get(pk=9)
        #objeto_tentativa = objeto_blocoJSX.Tentativa
        # objeto_tentativa_js = list(objeto_tentativa)  # important: convert the QuerySet to a list object


        #return JsonResponse({"objeto_tentativa": objeto_tentativa}) # também funciona
        #return HttpResponse(json.dumps(objeto_tentativa), content_type="application/json") # também funciona

"""