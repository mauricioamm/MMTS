from django.contrib import admin
from django.urls import path, include

from MtsApp.views import supdir_view, supesq_view, infesq_view, infdir_view, \
                        FimBloco_view, \
                        CarregarModelo_view, CarregarComparacoes_view,\
                        CarregarModeloAcertou_view, CarregarModeloErrou_view, FimBlocoAcertou_view, FimBlocoErrou_view,\
                        ResetSaida,Entrada_Iniciar,\
                        Entrada_login, Entrada_configuracoes,\
                        Entrada_relatorios, Entrada_sobre, LogoutView, Entrada, Comecar_bloco

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Entrada, name='url_entrada'),
    path('Janelas_SupEsq/', supesq_view, name='url_Janelas_SupEsq'),
    path('Janelas_SupDir/', supdir_view, name='url_Janelas_SupDir'),
    path('Janelas_InfEsq/', infesq_view, name='url_Janelas_InfEsq'),
    path('Janelas_InfDir/', infdir_view, name='url_Janelas_InfDir'),
    path('CarregarModelo/<int:pk>', CarregarModelo_view, name='url_CarregarModelo'),
    path('CarregarModeloAcertou/<int:pk>', CarregarModeloAcertou_view, name='url_CarregarModeloAcertou'),
    path('CarregarModeloErrou/<int:pk>', CarregarModeloErrou_view, name='url_CarregarModeloErrou'),
    path('CarregarComparacoes/<int:pk>', CarregarComparacoes_view, name='url_CarregarComparacoes'),
    path('FimBloco/', FimBloco_view, name='url_FimBloco'),
    path('FimBlocoAcertou/', FimBlocoAcertou_view, name='url_FimBlocoAcertou'),
    path('FimBlocoErrou/', FimBlocoErrou_view, name='url_FimBlocoErrou'),
    path('ResetSaida/', ResetSaida, name='url_ResetSaida'),
    path('Entrada_login/', Entrada_login, name='url_Entrada_login'),
    path('Entrada_Iniciar/', Entrada_Iniciar, name='url_Entrada_Iniciar'),
    path('ComecarBloco', Comecar_bloco, name= 'url_Comecar_bloco'),
    path('Entrada_configuracoes/', Entrada_configuracoes, name='url_Entrada_configuracoes'),
    path('Entrada_relatorios/', Entrada_relatorios, name='url_Entrada_relatorios'),
    path('Entrada_sobre/', Entrada_sobre, name='url_Entrada_sobre'),
    path('accounts/', include('django.contrib.auth.urls')),
    path("logout/", LogoutView.as_view(), name="logout"),

]

"""   
principal, principal_hidden, listagem, update, delete, criar, \
        teste_view, teste2_view, sessao_view, comecar_sessao_view, criar_tabela, clonar_model, \
        update, sessao_testar, parabens_view, entrada, teste_loop, LogoutView, listagem, janelas_teste, \
        ComecarBloco_view, Entrada_Um, BlocoJs_view, Js_View, ClickDjango, ChamaJson, ClickE1, ClickE2, ClickE3,\   

    #path('', Entrada_Um, name='url_Entrada_Um'),
    #path('ComecarBloco/', ComecarBloco_view, name='url_ComecarBloco'),
    #path('Janelas_Modelo/', modelo_view, name='url_Janelas_Modelo')
    #path('', listagem, name='url_listagem'),
    #path('janelas/', janelas, name='url_janelas'),
    #path('janelas_teste/', janelas_teste, name='url_janelas_teste'),
    path('BlocoJs/', BlocoJs_view, name='url_BlocoJs'),
    path('Js_View/', Js_View, name='url_Js_View'),
    path('ClickDjango/', ClickDjango, name='url_ClickDjango'),
    path('ClickE1/', ClickE1, name='url_ClickE1'),
    path('ClickE2/', ClickE2, name='url_ClickE2'),
    path('ClickE3/', ClickE3, name='url_ClickE3'),
    path('ChamaJson/', ChamaJson, name='url_ChamaJson'),
    path('', entrada, name='url_entrada'),
    path('criar/', criar, name= 'url_criar'),
    path('teste/', teste_view, name= 'url_teste_view'),
    path('teste2/', teste2_view, name= 'url_teste2_view'),
    path('teste_loop/', teste_loop, name= 'url_teste_loop_view'),
    path('criar_tabela/', criar_tabela, name= 'url_criar_tabela'),
    path('clonar/', clonar_model, name='url_clonar_model'),
    path('Parabens/', parabens_view, name='url_parabens_view'),
    path('update/<int:pk>/', update, name='url_update'),
    path('delete/<int:pk>/', delete, name='url_delete'),
    path('principal/<int:pk>/', principal, name='url_principal'),
    path('update/<int:pk>/', update, name='url_update'),
    path('sessao/<int:pk>/', sessao_view, name='url_sessao'),
    path('sessao_testar/<int:pk>/', sessao_testar, name='url_sessao_testar'),
    path('comecar_sessao/', comecar_sessao_view , name='url_comecar_sessao'),
    path('principal_hidden/<int:pk>/', principal_hidden, name='url_principal_hidden'),

"""


