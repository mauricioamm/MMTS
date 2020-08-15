from django.forms import ModelForm, Textarea
from django import forms

from .models import Cond1Bloco01Model, BlocoSaidaModel

class Cond1Bloco01Form(forms.ModelForm):
    class Meta:
        model = Cond1Bloco01Model
        fields = ['id', 'NomeBloco', 'Ordem', 'Tentativa', 'Modelo', 'SupEsq', 'SupDir', 'InfEsq', 'InfDir',
                  'Reforco', 'Correta', 'Procedimento']

class BlocoSaidaForm(forms.ModelForm):
    class Meta:
        model = BlocoSaidaModel
        fields = ['id', 'NomeBloco', 'Ordem', 'Tentativa', 'Modelo', 'SupEsq', 'SupDir', 'InfEsq', 'InfDir',
                  'Reforco', 'Correta', 'Procedimento', 'Escolheu', 'Acertou', 'RespVerb', 'Dia', 'Horario', 'Sessao',
                  'Corretas', 'Porcentagem']
