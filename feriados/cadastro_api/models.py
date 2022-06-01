from django.db import models


class FeriadoModel(models.Model):
    nome = models.CharField('feriado', max_length=100)
    data = models.DateField('data')

    def __str__(self):
        return self.nome
