from django.db import models

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

class ParticipanteModel(models.Model):
    id =            models.AutoField(primary_key=True)
    Participante =  models.CharField(max_length=200, blank=True, default='')
    Banco =  models.TextField(max_length=500, blank=True, default='')
    NomeCompleto = models.CharField(max_length=200, blank=True, default='')
    Idade = models.TextField(max_length=3, blank=True, default='')
    NomeProcedimento = models.TextField(max_length=50, blank=True, default='') #(ex."Condicao1")
    BlocoAtual = models.TextField(max_length=50, blank=True, default='') # atualização constante (necessário?)
    NoBlocoProximo = models.TextField(max_length=50, blank=True, default='') # atualização constante (necessário?)
    BlocoProximo = models.TextField(max_length=50, blank=True, default='') # atualização constante (necessário?)

    objetos = models.Manager()

class ProcedCond1Model(models.Model):
    id = models.AutoField(primary_key=True)
    NomeCondicao = models.TextField(max_length=50, blank=True, default='')
    NoBlocoUltimo = models.TextField(max_length=50, blank=True, default='')
    Bloco1Nome = models.TextField(max_length=50, blank=True, default='')
    Bloco1CriterioTotal = models.TextField(max_length=5, blank=True, default='')
    Bloco1CriterioTent = models.TextField(max_length=5, blank=True, default='')
    Bloco1CriterioSim = models.TextField(max_length=5, blank=True, default='')
    Bloco1CriterioNao = models.TextField(max_length=5, blank=True, default='')
    Bloco2Nome = models.TextField(max_length=50, blank=True, default='')
    Bloco2CriterioTotal = models.TextField(max_length=5, blank=True, default='')
    Bloco2CriterioTent = models.TextField(max_length=5, blank=True, default='')
    Bloco2CriterioSim = models.TextField(max_length=5, blank=True, default='')
    Bloco2CriterioNao = models.TextField(max_length=5, blank=True, default='')
    Bloco3Nome = models.TextField(max_length=50, blank=True, default='')
    Bloco3CriterioTotal = models.TextField(max_length=5, blank=True, default='')
    Bloco3CriterioTent = models.TextField(max_length=5, blank=True, default='')
    Bloco3CriterioSim = models.TextField(max_length=5, blank=True, default='')
    Bloco3CriterioNao = models.TextField(max_length=5, blank=True, default='')
    Bloco4Nome = models.TextField(max_length=50, blank=True, default='')
    Bloco4CriterioTotal = models.TextField(max_length=5, blank=True, default='')
    Bloco4CriterioTent = models.TextField(max_length=5, blank=True, default='')
    Bloco4CriterioSim = models.TextField(max_length=5, blank=True, default='')
    Bloco4CriterioNao = models.TextField(max_length=5, blank=True, default='')
    Bloco5Nome = models.TextField(max_length=50, blank=True, default='')
    Bloco5CriterioTotal = models.TextField(max_length=5, blank=True, default='')
    Bloco5CriterioTent = models.TextField(max_length=5, blank=True, default='')
    Bloco5CriterioSim = models.TextField(max_length=5, blank=True, default='')
    Bloco5CriterioNao = models.TextField(max_length=5, blank=True, default='')
    Bloco6Nome = models.TextField(max_length=50, blank=True, default='')
    Bloco6CriterioTotal = models.TextField(max_length=5, blank=True, default='')
    Bloco6CriterioTent = models.TextField(max_length=5, blank=True, default='')
    Bloco6CriterioSim = models.TextField(max_length=5, blank=True, default='')
    Bloco6CriterioNao = models.TextField(max_length=5, blank=True, default='')
    Bloco7Nome = models.TextField(max_length=50, blank=True, default='')
    Bloco7CriterioTotal = models.TextField(max_length=5, blank=True, default='')
    Bloco7CriterioTent = models.TextField(max_length=5, blank=True, default='')
    Bloco7CriterioSim = models.TextField(max_length=5, blank=True, default='')
    Bloco7CriterioNao = models.TextField(max_length=5, blank=True, default='')
    Bloco8Nome = models.TextField(max_length=50, blank=True, default='')
    Bloco8CriterioTotal = models.TextField(max_length=5, blank=True, default='')
    Bloco8CriterioTent = models.TextField(max_length=5, blank=True, default='')
    Bloco8CriterioSim = models.TextField(max_length=5, blank=True, default='')
    Bloco8CriterioNao = models.TextField(max_length=5, blank=True, default='')
    Bloco9Nome = models.TextField(max_length=50, blank=True, default='')
    Bloco9CriterioTotal = models.TextField(max_length=5, blank=True, default='')
    Bloco9CriterioTent = models.TextField(max_length=5, blank=True, default='')
    Bloco9CriterioSim = models.TextField(max_length=5, blank=True, default='')
    Bloco9CriterioNao = models.TextField(max_length=5, blank=True, default='')
    Bloco10Nome = models.TextField(max_length=50, blank=True, default='')
    Bloco10CriterioTotal = models.TextField(max_length=5, blank=True, default='')
    Bloco10CriterioTent = models.TextField(max_length=5, blank=True, default='')
    Bloco10CriterioSim = models.TextField(max_length=5, blank=True, default='')
    Bloco10CriterioNao = models.TextField(max_length=5, blank=True, default='')
    Bloco11Nome = models.TextField(max_length=50, blank=True, default='')
    Bloco11CriterioTotal = models.TextField(max_length=5, blank=True, default='')
    Bloco11CriterioTent = models.TextField(max_length=5, blank=True, default='')
    Bloco11CriterioSim = models.TextField(max_length=5, blank=True, default='')
    Bloco11CriterioNao = models.TextField(max_length=5, blank=True, default='')

    objetos = models.Manager()

class ProcedCond2Model(models.Model):
    id = models.AutoField(primary_key=True)
    NomeCondicao = models.TextField(max_length=50, blank=True, default='')
    NoBlocoUltimo = models.TextField(max_length=50, blank=True, default='')
    Bloco1Nome = models.TextField(max_length=50, blank=True, default='')
    Bloco1CriterioTotal = models.TextField(max_length=5, blank=True, default='')
    Bloco1CriterioTent = models.TextField(max_length=5, blank=True, default='')
    Bloco1CriterioSim = models.TextField(max_length=5, blank=True, default='')
    Bloco1CriterioNao = models.TextField(max_length=5, blank=True, default='')
    Bloco2Nome = models.TextField(max_length=50, blank=True, default='')
    Bloco2CriterioTotal = models.TextField(max_length=5, blank=True, default='')
    Bloco2CriterioTent = models.TextField(max_length=5, blank=True, default='')
    Bloco2CriterioSim = models.TextField(max_length=5, blank=True, default='')
    Bloco2CriterioNao = models.TextField(max_length=5, blank=True, default='')
    Bloco3Nome = models.TextField(max_length=50, blank=True, default='')
    Bloco3CriterioTotal = models.TextField(max_length=5, blank=True, default='')
    Bloco3CriterioTent = models.TextField(max_length=5, blank=True, default='')
    Bloco3CriterioSim = models.TextField(max_length=5, blank=True, default='')
    Bloco3CriterioNao = models.TextField(max_length=5, blank=True, default='')
    Bloco4Nome = models.TextField(max_length=50, blank=True, default='')
    Bloco4CriterioTotal = models.TextField(max_length=5, blank=True, default='')
    Bloco4CriterioTent = models.TextField(max_length=5, blank=True, default='')
    Bloco4CriterioSim = models.TextField(max_length=5, blank=True, default='')
    Bloco4CriterioNao = models.TextField(max_length=5, blank=True, default='')
    Bloco5Nome = models.TextField(max_length=50, blank=True, default='')
    Bloco5CriterioTotal = models.TextField(max_length=5, blank=True, default='')
    Bloco5CriterioTent = models.TextField(max_length=5, blank=True, default='')
    Bloco5CriterioSim = models.TextField(max_length=5, blank=True, default='')
    Bloco5CriterioNao = models.TextField(max_length=5, blank=True, default='')
    Bloco6Nome = models.TextField(max_length=50, blank=True, default='')
    Bloco6CriterioTotal = models.TextField(max_length=5, blank=True, default='')
    Bloco6CriterioTent = models.TextField(max_length=5, blank=True, default='')
    Bloco6CriterioSim = models.TextField(max_length=5, blank=True, default='')
    Bloco6CriterioNao = models.TextField(max_length=5, blank=True, default='')
    Bloco7Nome = models.TextField(max_length=50, blank=True, default='')
    Bloco7CriterioTotal = models.TextField(max_length=5, blank=True, default='')
    Bloco7CriterioTent = models.TextField(max_length=5, blank=True, default='')
    Bloco7CriterioSim = models.TextField(max_length=5, blank=True, default='')
    Bloco7CriterioNao = models.TextField(max_length=5, blank=True, default='')
    Bloco8Nome = models.TextField(max_length=50, blank=True, default='')
    Bloco8CriterioTotal = models.TextField(max_length=5, blank=True, default='')
    Bloco8CriterioTent = models.TextField(max_length=5, blank=True, default='')
    Bloco8CriterioSim = models.TextField(max_length=5, blank=True, default='')
    Bloco8CriterioNao = models.TextField(max_length=5, blank=True, default='')
    Bloco9Nome = models.TextField(max_length=50, blank=True, default='')
    Bloco9CriterioTotal = models.TextField(max_length=5, blank=True, default='')
    Bloco9CriterioTent = models.TextField(max_length=5, blank=True, default='')
    Bloco9CriterioSim = models.TextField(max_length=5, blank=True, default='')
    Bloco9CriterioNao = models.TextField(max_length=5, blank=True, default='')
    Bloco10Nome = models.TextField(max_length=50, blank=True, default='')
    Bloco10CriterioTotal = models.TextField(max_length=5, blank=True, default='')
    Bloco10CriterioTent = models.TextField(max_length=5, blank=True, default='')
    Bloco10CriterioSim = models.TextField(max_length=5, blank=True, default='')
    Bloco10CriterioNao = models.TextField(max_length=5, blank=True, default='')
    Bloco11Nome = models.TextField(max_length=50, blank=True, default='')
    Bloco11CriterioTotal = models.TextField(max_length=5, blank=True, default='')
    Bloco11CriterioTent = models.TextField(max_length=5, blank=True, default='')
    Bloco11CriterioSim = models.TextField(max_length=5, blank=True, default='')
    Bloco11CriterioNao = models.TextField(max_length=5, blank=True, default='')
    Bloco12Nome = models.TextField(max_length=50, blank=True, default='')
    Bloco12CriterioTotal = models.TextField(max_length=5, blank=True, default='')
    Bloco12CriterioTent = models.TextField(max_length=5, blank=True, default='')
    Bloco12CriterioSim = models.TextField(max_length=5, blank=True, default='')
    Bloco12CriterioNao = models.TextField(max_length=5, blank=True, default='')
    Bloco13Nome = models.TextField(max_length=50, blank=True, default='')
    Bloco13CriterioTotal = models.TextField(max_length=5, blank=True, default='')
    Bloco13CriterioTent = models.TextField(max_length=5, blank=True, default='')
    Bloco13CriterioSim = models.TextField(max_length=5, blank=True, default='')
    Bloco13CriterioNao = models.TextField(max_length=5, blank=True, default='')
    Bloco14Nome = models.TextField(max_length=50, blank=True, default='')
    Bloco14CriterioTotal = models.TextField(max_length=5, blank=True, default='')
    Bloco14CriterioTent = models.TextField(max_length=5, blank=True, default='')
    Bloco14CriterioSim = models.TextField(max_length=5, blank=True, default='')
    Bloco14CriterioNao = models.TextField(max_length=5, blank=True, default='')
    Bloco15Nome = models.TextField(max_length=50, blank=True, default='')
    Bloco15CriterioTotal = models.TextField(max_length=5, blank=True, default='')
    Bloco15CriterioTent = models.TextField(max_length=5, blank=True, default='')
    Bloco15CriterioSim = models.TextField(max_length=5, blank=True, default='')
    Bloco15CriterioNao = models.TextField(max_length=5, blank=True, default='')
    Bloco16Nome = models.TextField(max_length=50, blank=True, default='')
    Bloco16CriterioTotal = models.TextField(max_length=5, blank=True, default='')
    Bloco16CriterioTent = models.TextField(max_length=5, blank=True, default='')
    Bloco16CriterioSim = models.TextField(max_length=5, blank=True, default='')
    Bloco16CriterioNao = models.TextField(max_length=5, blank=True, default='')
    Bloco17Nome = models.TextField(max_length=50, blank=True, default='')
    Bloco17CriterioTotal = models.TextField(max_length=5, blank=True, default='')
    Bloco17CriterioTent = models.TextField(max_length=5, blank=True, default='')
    Bloco17CriterioSim = models.TextField(max_length=5, blank=True, default='')
    Bloco17CriterioNao = models.TextField(max_length=5, blank=True, default='')
    Bloco18Nome = models.TextField(max_length=50, blank=True, default='')
    Bloco18CriterioTotal = models.TextField(max_length=5, blank=True, default='')
    Bloco18CriterioTent = models.TextField(max_length=5, blank=True, default='')
    Bloco18CriterioSim = models.TextField(max_length=5, blank=True, default='')
    Bloco18CriterioNao = models.TextField(max_length=5, blank=True, default='')
    Bloco19Nome = models.TextField(max_length=50, blank=True, default='')
    Bloco19CriterioTotal = models.TextField(max_length=5, blank=True, default='')
    Bloco19CriterioTent = models.TextField(max_length=5, blank=True, default='')
    Bloco19CriterioSim = models.TextField(max_length=5, blank=True, default='')
    Bloco19CriterioNao = models.TextField(max_length=5, blank=True, default='')
    Bloco20Nome = models.TextField(max_length=50, blank=True, default='')
    Bloco20CriterioTotal = models.TextField(max_length=5, blank=True, default='')
    Bloco20CriterioTent = models.TextField(max_length=5, blank=True, default='')
    Bloco20CriterioSim = models.TextField(max_length=5, blank=True, default='')
    Bloco20CriterioNao = models.TextField(max_length=5, blank=True, default='')
    Bloco21Nome = models.TextField(max_length=50, blank=True, default='')
    Bloco21CriterioTotal = models.TextField(max_length=5, blank=True, default='')
    Bloco21CriterioTent = models.TextField(max_length=5, blank=True, default='')
    Bloco21CriterioSim = models.TextField(max_length=5, blank=True, default='')
    Bloco21CriterioNao = models.TextField(max_length=5, blank=True, default='')
    Bloco22Nome = models.TextField(max_length=50, blank=True, default='')
    Bloco22CriterioTotal = models.TextField(max_length=5, blank=True, default='')
    Bloco22CriterioTent = models.TextField(max_length=5, blank=True, default='')
    Bloco22CriterioSim = models.TextField(max_length=5, blank=True, default='')
    Bloco22CriterioNao = models.TextField(max_length=5, blank=True, default='')
    Bloco23Nome = models.TextField(max_length=50, blank=True, default='')
    Bloco23CriterioTotal = models.TextField(max_length=5, blank=True, default='')
    Bloco23CriterioTent = models.TextField(max_length=5, blank=True, default='')
    Bloco23CriterioSim = models.TextField(max_length=5, blank=True, default='')
    Bloco23CriterioNao = models.TextField(max_length=5, blank=True, default='')
    Bloco24Nome = models.TextField(max_length=50, blank=True, default='')
    Bloco24CriterioTotal = models.TextField(max_length=5, blank=True, default='')
    Bloco24CriterioTent = models.TextField(max_length=5, blank=True, default='')
    Bloco24CriterioSim = models.TextField(max_length=5, blank=True, default='')
    Bloco24CriterioNao = models.TextField(max_length=5, blank=True, default='')
    Bloco25Nome = models.TextField(max_length=50, blank=True, default='')
    Bloco25CriterioTotal = models.TextField(max_length=5, blank=True, default='')
    Bloco25CriterioTent = models.TextField(max_length=5, blank=True, default='')
    Bloco25CriterioSim = models.TextField(max_length=5, blank=True, default='')
    Bloco25CriterioNao = models.TextField(max_length=5, blank=True, default='')
    Bloco26Nome = models.TextField(max_length=50, blank=True, default='')
    Bloco26CriterioTotal = models.TextField(max_length=5, blank=True, default='')
    Bloco26CriterioTent = models.TextField(max_length=5, blank=True, default='')
    Bloco26CriterioSim = models.TextField(max_length=5, blank=True, default='')
    Bloco26CriterioNao = models.TextField(max_length=5, blank=True, default='')
    Bloco27Nome = models.TextField(max_length=50, blank=True, default='')
    Bloco27CriterioTotal = models.TextField(max_length=5, blank=True, default='')
    Bloco27CriterioTent = models.TextField(max_length=5, blank=True, default='')
    Bloco27CriterioSim = models.TextField(max_length=5, blank=True, default='')
    Bloco27CriterioNao = models.TextField(max_length=5, blank=True, default='')
    Bloco28Nome = models.TextField(max_length=50, blank=True, default='')
    Bloco28CriterioTotal = models.TextField(max_length=5, blank=True, default='')
    Bloco28CriterioTent = models.TextField(max_length=5, blank=True, default='')
    Bloco28CriterioSim = models.TextField(max_length=5, blank=True, default='')
    Bloco28CriterioNao = models.TextField(max_length=5, blank=True, default='')
    Bloco29Nome = models.TextField(max_length=50, blank=True, default='')
    Bloco29CriterioTotal = models.TextField(max_length=5, blank=True, default='')
    Bloco29CriterioTent = models.TextField(max_length=5, blank=True, default='')
    Bloco29CriterioSim = models.TextField(max_length=5, blank=True, default='')
    Bloco29CriterioNao = models.TextField(max_length=5, blank=True, default='')
    Bloco30Nome = models.TextField(max_length=50, blank=True, default='')
    Bloco30CriterioTotal = models.TextField(max_length=5, blank=True, default='')
    Bloco30CriterioTent = models.TextField(max_length=5, blank=True, default='')
    Bloco30CriterioSim = models.TextField(max_length=5, blank=True, default='')
    Bloco30CriterioNao = models.TextField(max_length=5, blank=True, default='')
    Bloco31Nome = models.TextField(max_length=50, blank=True, default='')
    Bloco31CriterioTotal = models.TextField(max_length=5, blank=True, default='')
    Bloco31CriterioTent = models.TextField(max_length=5, blank=True, default='')
    Bloco31CriterioSim = models.TextField(max_length=5, blank=True, default='')
    Bloco31CriterioNao = models.TextField(max_length=5, blank=True, default='')
    Bloco32Nome = models.TextField(max_length=50, blank=True, default='')
    Bloco32CriterioTotal = models.TextField(max_length=5, blank=True, default='')
    Bloco32CriterioTent = models.TextField(max_length=5, blank=True, default='')
    Bloco32CriterioSim = models.TextField(max_length=5, blank=True, default='')
    Bloco32CriterioNao = models.TextField(max_length=5, blank=True, default='')

    objetos = models.Manager()

class Cond1Bloco01Model(models.Model):
    id =            models.AutoField(primary_key=True)
    NomeBloco = models.TextField(max_length=50, blank=True, default='')
    Ordem =         models.CharField(max_length=3, blank=True, default='')
    Tentativa =     models.CharField(max_length=10, blank=True, default='')
    TipoTentativa = models.CharField(max_length=10, blank=True, default='')
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

class Cond1Bloco02Model(models.Model):
    id =            models.AutoField(primary_key=True)
    NomeBloco = models.TextField(max_length=50, blank=True, default='')
    Ordem =         models.CharField(max_length=3, blank=True, default='')
    Tentativa =     models.CharField(max_length=10, blank=True, default='')
    TipoTentativa = models.CharField(max_length=10, blank=True, default='')
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

class Cond1Bloco03Model(models.Model):
    id =            models.AutoField(primary_key=True)
    NomeBloco = models.TextField(max_length=50, blank=True, default='')
    Ordem =         models.CharField(max_length=3, blank=True, default='')
    Tentativa =     models.CharField(max_length=10, blank=True, default='')
    TipoTentativa = models.CharField(max_length=10, blank=True, default='')
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


class Cond1Bloco04Model(models.Model):
    id =            models.AutoField(primary_key=True)
    NomeBloco = models.TextField(max_length=50, blank=True, default='')
    Ordem =         models.CharField(max_length=3, blank=True, default='')
    Tentativa =     models.CharField(max_length=10, blank=True, default='')
    TipoTentativa = models.CharField(max_length=10, blank=True, default='')
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


class Cond1Bloco05Model(models.Model):
    id =            models.AutoField(primary_key=True)
    NomeBloco = models.TextField(max_length=50, blank=True, default='')
    Ordem =         models.CharField(max_length=3, blank=True, default='')
    Tentativa =     models.CharField(max_length=10, blank=True, default='')
    TipoTentativa = models.CharField(max_length=10, blank=True, default='')
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


class Cond1Bloco06Model(models.Model):
    id =            models.AutoField(primary_key=True)
    NomeBloco = models.TextField(max_length=50, blank=True, default='')
    Ordem =         models.CharField(max_length=3, blank=True, default='')
    Tentativa =     models.CharField(max_length=10, blank=True, default='')
    TipoTentativa = models.CharField(max_length=10, blank=True, default='')
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

class Cond1Bloco07Model(models.Model):
    id =            models.AutoField(primary_key=True)
    NomeBloco = models.TextField(max_length=50, blank=True, default='')
    Ordem =         models.CharField(max_length=3, blank=True, default='')
    Tentativa =     models.CharField(max_length=10, blank=True, default='')
    TipoTentativa = models.CharField(max_length=10, blank=True, default='')
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


class Cond1Bloco08Model(models.Model):
    id =            models.AutoField(primary_key=True)
    NomeBloco = models.TextField(max_length=50, blank=True, default='')
    Ordem =         models.CharField(max_length=3, blank=True, default='')
    Tentativa =     models.CharField(max_length=10, blank=True, default='')
    TipoTentativa = models.CharField(max_length=10, blank=True, default='')
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


class Cond1Bloco09Model(models.Model):
    id =            models.AutoField(primary_key=True)
    NomeBloco = models.TextField(max_length=50, blank=True, default='')
    Ordem =         models.CharField(max_length=3, blank=True, default='')
    Tentativa =     models.CharField(max_length=10, blank=True, default='')
    TipoTentativa = models.CharField(max_length=10, blank=True, default='')
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


class Cond1Bloco10Model(models.Model):
    id =            models.AutoField(primary_key=True)
    NomeBloco = models.TextField(max_length=50, blank=True, default='')
    Ordem =         models.CharField(max_length=3, blank=True, default='')
    Tentativa =     models.CharField(max_length=10, blank=True, default='')
    TipoTentativa = models.CharField(max_length=10, blank=True, default='')
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


class Cond1Bloco11Model(models.Model):
    id =            models.AutoField(primary_key=True)
    NomeBloco = models.TextField(max_length=50, blank=True, default='')
    Ordem =         models.CharField(max_length=3, blank=True, default='')
    Tentativa =     models.CharField(max_length=10, blank=True, default='')
    TipoTentativa = models.CharField(max_length=10, blank=True, default='')
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

class Cond2Bloco01Model(models.Model):
    id =            models.AutoField(primary_key=True)
    NomeBloco = models.TextField(max_length=50, blank=True, default='')
    Ordem =         models.CharField(max_length=3, blank=True, default='')
    Tentativa =     models.CharField(max_length=10, blank=True, default='')
    TipoTentativa = models.CharField(max_length=10, blank=True, default='')
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

class Cond2Bloco02Model(models.Model):
    id =            models.AutoField(primary_key=True)
    NomeBloco = models.TextField(max_length=50, blank=True, default='')
    Ordem =         models.CharField(max_length=3, blank=True, default='')
    Tentativa =     models.CharField(max_length=10, blank=True, default='')
    TipoTentativa = models.CharField(max_length=10, blank=True, default='')
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

class Cond2Bloco03Model(models.Model):
    id =            models.AutoField(primary_key=True)
    NomeBloco = models.TextField(max_length=50, blank=True, default='')
    Ordem =         models.CharField(max_length=3, blank=True, default='')
    Tentativa =     models.CharField(max_length=10, blank=True, default='')
    TipoTentativa = models.CharField(max_length=10, blank=True, default='')
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

class Cond2Bloco04Model(models.Model):
    id =            models.AutoField(primary_key=True)
    NomeBloco = models.TextField(max_length=50, blank=True, default='')
    Ordem =         models.CharField(max_length=3, blank=True, default='')
    Tentativa =     models.CharField(max_length=10, blank=True, default='')
    TipoTentativa = models.CharField(max_length=10, blank=True, default='')
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

class Cond2Bloco05Model(models.Model):
    id =            models.AutoField(primary_key=True)
    NomeBloco = models.TextField(max_length=50, blank=True, default='')
    Ordem =         models.CharField(max_length=3, blank=True, default='')
    Tentativa =     models.CharField(max_length=10, blank=True, default='')
    TipoTentativa = models.CharField(max_length=10, blank=True, default='')
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

class Cond2Bloco06Model(models.Model):
    id =            models.AutoField(primary_key=True)
    NomeBloco = models.TextField(max_length=50, blank=True, default='')
    Ordem =         models.CharField(max_length=3, blank=True, default='')
    Tentativa =     models.CharField(max_length=10, blank=True, default='')
    TipoTentativa = models.CharField(max_length=10, blank=True, default='')
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

class Cond2Bloco07Model(models.Model):
    id =            models.AutoField(primary_key=True)
    NomeBloco = models.TextField(max_length=50, blank=True, default='')
    Ordem =         models.CharField(max_length=3, blank=True, default='')
    Tentativa =     models.CharField(max_length=10, blank=True, default='')
    TipoTentativa = models.CharField(max_length=10, blank=True, default='')
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

class Cond2Bloco08Model(models.Model):
    id =            models.AutoField(primary_key=True)
    NomeBloco = models.TextField(max_length=50, blank=True, default='')
    Ordem =         models.CharField(max_length=3, blank=True, default='')
    Tentativa =     models.CharField(max_length=10, blank=True, default='')
    TipoTentativa = models.CharField(max_length=10, blank=True, default='')
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

class Cond2Bloco09Model(models.Model):
    id =            models.AutoField(primary_key=True)
    NomeBloco = models.TextField(max_length=50, blank=True, default='')
    Ordem =         models.CharField(max_length=3, blank=True, default='')
    Tentativa =     models.CharField(max_length=10, blank=True, default='')
    TipoTentativa = models.CharField(max_length=10, blank=True, default='')
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

class Cond2Bloco10Model(models.Model):
    id =            models.AutoField(primary_key=True)
    NomeBloco = models.TextField(max_length=50, blank=True, default='')
    Ordem =         models.CharField(max_length=3, blank=True, default='')
    Tentativa =     models.CharField(max_length=10, blank=True, default='')
    TipoTentativa = models.CharField(max_length=10, blank=True, default='')
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

class Cond2Bloco11Model(models.Model):
    id =            models.AutoField(primary_key=True)
    NomeBloco = models.TextField(max_length=50, blank=True, default='')
    Ordem =         models.CharField(max_length=3, blank=True, default='')
    Tentativa =     models.CharField(max_length=10, blank=True, default='')
    TipoTentativa = models.CharField(max_length=10, blank=True, default='')
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

class Cond2Bloco12Model(models.Model):
    id =            models.AutoField(primary_key=True)
    NomeBloco = models.TextField(max_length=50, blank=True, default='')
    Ordem =         models.CharField(max_length=3, blank=True, default='')
    Tentativa =     models.CharField(max_length=10, blank=True, default='')
    TipoTentativa = models.CharField(max_length=10, blank=True, default='')
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

class Cond2Bloco13Model(models.Model):
    id =            models.AutoField(primary_key=True)
    NomeBloco = models.TextField(max_length=50, blank=True, default='')
    Ordem =         models.CharField(max_length=3, blank=True, default='')
    Tentativa =     models.CharField(max_length=10, blank=True, default='')
    TipoTentativa = models.CharField(max_length=10, blank=True, default='')
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

class Cond2Bloco14Model(models.Model):
    id =            models.AutoField(primary_key=True)
    NomeBloco = models.TextField(max_length=50, blank=True, default='')
    Ordem =         models.CharField(max_length=3, blank=True, default='')
    Tentativa =     models.CharField(max_length=10, blank=True, default='')
    TipoTentativa = models.CharField(max_length=10, blank=True, default='')
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


class Cond2Bloco15Model(models.Model):
    id = models.AutoField(primary_key=True)
    NomeBloco = models.TextField(max_length=50, blank=True, default='')
    Ordem = models.CharField(max_length=3, blank=True, default='')
    Tentativa = models.CharField(max_length=10, blank=True, default='')
    TipoTentativa = models.CharField(max_length=10, blank=True, default='')
    Modelo = models.TextField(max_length=100, blank=True, default='')
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


class Cond2Bloco16Model(models.Model):
    id = models.AutoField(primary_key=True)
    NomeBloco = models.TextField(max_length=50, blank=True, default='')
    Ordem = models.CharField(max_length=3, blank=True, default='')
    Tentativa = models.CharField(max_length=10, blank=True, default='')
    TipoTentativa = models.CharField(max_length=10, blank=True, default='')
    Modelo = models.TextField(max_length=100, blank=True, default='')
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


class Cond2Bloco17Model(models.Model):
    id = models.AutoField(primary_key=True)
    NomeBloco = models.TextField(max_length=50, blank=True, default='')
    Ordem = models.CharField(max_length=3, blank=True, default='')
    Tentativa = models.CharField(max_length=10, blank=True, default='')
    TipoTentativa = models.CharField(max_length=10, blank=True, default='')
    Modelo = models.TextField(max_length=100, blank=True, default='')
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


class Cond2Bloco18Model(models.Model):
    id = models.AutoField(primary_key=True)
    NomeBloco = models.TextField(max_length=50, blank=True, default='')
    Ordem = models.CharField(max_length=3, blank=True, default='')
    Tentativa = models.CharField(max_length=10, blank=True, default='')
    TipoTentativa = models.CharField(max_length=10, blank=True, default='')
    Modelo = models.TextField(max_length=100, blank=True, default='')
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


class Cond2Bloco19Model(models.Model):
    id = models.AutoField(primary_key=True)
    NomeBloco = models.TextField(max_length=50, blank=True, default='')
    Ordem = models.CharField(max_length=3, blank=True, default='')
    Tentativa = models.CharField(max_length=10, blank=True, default='')
    TipoTentativa = models.CharField(max_length=10, blank=True, default='')
    Modelo = models.TextField(max_length=100, blank=True, default='')
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


class Cond2Bloco20Model(models.Model):
    id = models.AutoField(primary_key=True)
    NomeBloco = models.TextField(max_length=50, blank=True, default='')
    Ordem = models.CharField(max_length=3, blank=True, default='')
    Tentativa = models.CharField(max_length=10, blank=True, default='')
    TipoTentativa = models.CharField(max_length=10, blank=True, default='')
    Modelo = models.TextField(max_length=100, blank=True, default='')
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


class Cond2Bloco21Model(models.Model):
    id = models.AutoField(primary_key=True)
    NomeBloco = models.TextField(max_length=50, blank=True, default='')
    Ordem = models.CharField(max_length=3, blank=True, default='')
    Tentativa = models.CharField(max_length=10, blank=True, default='')
    TipoTentativa = models.CharField(max_length=10, blank=True, default='')
    Modelo = models.TextField(max_length=100, blank=True, default='')
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


class Cond2Bloco22Model(models.Model):
    id = models.AutoField(primary_key=True)
    NomeBloco = models.TextField(max_length=50, blank=True, default='')
    Ordem = models.CharField(max_length=3, blank=True, default='')
    Tentativa = models.CharField(max_length=10, blank=True, default='')
    TipoTentativa = models.CharField(max_length=10, blank=True, default='')
    Modelo = models.TextField(max_length=100, blank=True, default='')
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


class Cond2Bloco23Model(models.Model):
    id = models.AutoField(primary_key=True)
    NomeBloco = models.TextField(max_length=50, blank=True, default='')
    Ordem = models.CharField(max_length=3, blank=True, default='')
    Tentativa = models.CharField(max_length=10, blank=True, default='')
    TipoTentativa = models.CharField(max_length=10, blank=True, default='')
    Modelo = models.TextField(max_length=100, blank=True, default='')
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


class Cond2Bloco24Model(models.Model):
    id = models.AutoField(primary_key=True)
    NomeBloco = models.TextField(max_length=50, blank=True, default='')
    Ordem = models.CharField(max_length=3, blank=True, default='')
    Tentativa = models.CharField(max_length=10, blank=True, default='')
    TipoTentativa = models.CharField(max_length=10, blank=True, default='')
    Modelo = models.TextField(max_length=100, blank=True, default='')
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


class Cond2Bloco25Model(models.Model):
    id = models.AutoField(primary_key=True)
    NomeBloco = models.TextField(max_length=50, blank=True, default='')
    Ordem = models.CharField(max_length=3, blank=True, default='')
    Tentativa = models.CharField(max_length=10, blank=True, default='')
    TipoTentativa = models.CharField(max_length=10, blank=True, default='')
    Modelo = models.TextField(max_length=100, blank=True, default='')
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


class Cond2Bloco26Model(models.Model):
    id = models.AutoField(primary_key=True)
    NomeBloco = models.TextField(max_length=50, blank=True, default='')
    Ordem = models.CharField(max_length=3, blank=True, default='')
    Tentativa = models.CharField(max_length=10, blank=True, default='')
    TipoTentativa = models.CharField(max_length=10, blank=True, default='')
    Modelo = models.TextField(max_length=100, blank=True, default='')
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


class Cond2Bloco27Model(models.Model):
    id = models.AutoField(primary_key=True)
    NomeBloco = models.TextField(max_length=50, blank=True, default='')
    Ordem = models.CharField(max_length=3, blank=True, default='')
    Tentativa = models.CharField(max_length=10, blank=True, default='')
    TipoTentativa = models.CharField(max_length=10, blank=True, default='')
    Modelo = models.TextField(max_length=100, blank=True, default='')
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


class Cond2Bloco28Model(models.Model):
    id = models.AutoField(primary_key=True)
    NomeBloco = models.TextField(max_length=50, blank=True, default='')
    Ordem = models.CharField(max_length=3, blank=True, default='')
    Tentativa = models.CharField(max_length=10, blank=True, default='')
    TipoTentativa = models.CharField(max_length=10, blank=True, default='')
    Modelo = models.TextField(max_length=100, blank=True, default='')
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

class Cond2Bloco29Model(models.Model):
    id = models.AutoField(primary_key=True)
    NomeBloco = models.TextField(max_length=50, blank=True, default='')
    Ordem = models.CharField(max_length=3, blank=True, default='')
    Tentativa = models.CharField(max_length=10, blank=True, default='')
    TipoTentativa = models.CharField(max_length=10, blank=True, default='')
    Modelo = models.TextField(max_length=100, blank=True, default='')
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

class Cond2Bloco30Model(models.Model):
    id = models.AutoField(primary_key=True)
    NomeBloco = models.TextField(max_length=50, blank=True, default='')
    Ordem = models.CharField(max_length=3, blank=True, default='')
    Tentativa = models.CharField(max_length=10, blank=True, default='')
    TipoTentativa = models.CharField(max_length=10, blank=True, default='')
    Modelo = models.TextField(max_length=100, blank=True, default='')
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

class Cond2Bloco31Model(models.Model):
    id = models.AutoField(primary_key=True)
    NomeBloco = models.TextField(max_length=50, blank=True, default='')
    Ordem = models.CharField(max_length=3, blank=True, default='')
    Tentativa = models.CharField(max_length=10, blank=True, default='')
    TipoTentativa = models.CharField(max_length=10, blank=True, default='')
    Modelo = models.TextField(max_length=100, blank=True, default='')
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

class Cond2Bloco32Model(models.Model):
    id = models.AutoField(primary_key=True)
    NomeBloco = models.TextField(max_length=50, blank=True, default='')
    Ordem = models.CharField(max_length=3, blank=True, default='')
    Tentativa = models.CharField(max_length=10, blank=True, default='')
    TipoTentativa = models.CharField(max_length=10, blank=True, default='')
    Modelo = models.TextField(max_length=100, blank=True, default='')
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

class Cond2Bloco33Model(models.Model):
    id = models.AutoField(primary_key=True)
    NomeBloco = models.TextField(max_length=50, blank=True, default='')
    Ordem = models.CharField(max_length=3, blank=True, default='')
    Tentativa = models.CharField(max_length=10, blank=True, default='')
    TipoTentativa = models.CharField(max_length=10, blank=True, default='')
    Modelo = models.TextField(max_length=100, blank=True, default='')
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