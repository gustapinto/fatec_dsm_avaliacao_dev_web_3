from django.shortcuts import render, HttpResponse

from .models import FeriadoModel
from .utils.FeriadosAPI import FeriadoAPI


def cadastra_feriados(request):
    api = FeriadoAPI(2022)

    for feriado in api.feriados:
        nome, data = feriado

        cadastro = FeriadoModel(nome=nome, data=data)
        cadastro.save()

    return HttpResponse('')
