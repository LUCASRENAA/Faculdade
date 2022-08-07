from django.db import models

# Create your models here.


from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

class OrgaoDonatario(models.Model):
    nome = models.CharField(max_length=50)
    endereco = models.CharField(max_length=50)
    telefone = models.CharField(max_length=50)
    horarioFuncionamento = models.CharField(max_length=50)
    descricao = models.CharField(max_length=50)

class OrgaoFiscalizador(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=50)



class Lote(models.Model):
    dataEntrega = models.CharField(max_length=50)
    observacao = models.CharField(max_length=50)
    orgaoDonatario = models.ForeignKey(OrgaoDonatario, models.CASCADE)
    orgaoFiscalizador = models.ForeignKey(OrgaoFiscalizador, models.CASCADE)



class Produto(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=50)
    lote = models.ForeignKey(Lote, models.CASCADE)

#usuario = models.ForeignKey(User, models.CASCADE)

