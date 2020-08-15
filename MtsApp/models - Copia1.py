from django.db import models

class Cond1Bloco01Model(models.Model):
    id =            models.AutoField(primary_key=True)
    NomeBloco = models.TextField(max_length=50, blank=True, default='')
    Ordem =         models.CharField(max_length=3, blank=True, default='')
    Tentativa =     models.CharField(max_length=10, blank=True, default='')
    Modelo=         models.TextField(max_length=100, blank=True, default='')
    SupEsq = models.TextField(max_length=100, blank=True, default='')
    SupDir = models.TextField(max_length=100, blank=True, default='')
    InfEsq = models.TextField(max_length=100, blank=True, default='')
    InfDir = models.TextField(max_length=100, blank=True, default='')
    Reforco = models.TextField(max_length=3, blank=True, default='')
    Correta = models.TextField(max_length=3, blank=True, default='')
    Procedimento = models.TextField(max_length=50, blank=True, default='')


    def __str__(self):
        return self.Ordem

    objetos = models.Manager()

class BlocoSaidaModel(models.Model):
    id = models.AutoField(primary_key=True)
    NomeBloco = models.TextField(max_length=50, blank=True, default='')
    Participante = models.CharField(max_length=100, blank=True, default='')
    Ordem = models.CharField(max_length=3, blank=True, default='')
    Tentativa = models.CharField(max_length=10, blank=True, default='')
    Modelo = models.TextField(max_length=100, blank=True, default='')
    SupEsq = models.TextField(max_length=100, blank=True, default='')
    SupDir = models.TextField(max_length=100, blank=True, default='')
    InfEsq = models.TextField(max_length=100, blank=True, default='')
    InfDir = models.TextField(max_length=100, blank=True, default='')
    Reforco = models.TextField(max_length=3, blank=True, default='')
    Correta = models.TextField(max_length=3, blank=True, default='')
    Escolheu = models.TextField(max_length=3, blank=True, default='')
    Acertou = models.TextField(max_length=3, blank=True, default='')
    RespVerb = models.TextField(max_length=100, blank=True, default='')
    Dia = models.CharField(max_length=20, blank=True, default='')
    Horario = models.TextField(max_length=20, blank=True, default='')
    Sessao = models.CharField(max_length=3, blank=True, default='')
    Corretas = models.CharField(max_length=3, blank=True, default='0')
    Porcentagem = models.CharField(max_length=3, blank=True, default='0')
    Procedimento = models.CharField(max_length=40, blank=True, default='1')

    def __str__(self):
       return self.Ordem

    objetos = models.Manager()