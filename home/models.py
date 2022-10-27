from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models


class Cidade(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Detalhes(models.Model):
    detalhe = nome = models.ForeignKey(Cidade, on_delete=models.DO_NOTHING)
    nome = models.CharField(max_length=50)
    nullable = models.BooleanField(default=True)
    dataFundacao = models.DateTimeField(auto_add=True)
    populacaoEstimada = models.IntegerField()
    altitude = models.IntegerField()
    idh = models.DecimalField(decimal_places=1, max_digits=10)
    site = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
