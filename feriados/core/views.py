from django.shortcuts import render, HttpResponse
from datetime import date
from django.shortcuts import render
from cadastro_api.models import FeriadoModel

def verificar(request):
    hoje = date.today()

    try:
        feriados = FeriadoModel.objects.all().filter(data=hoje)
    except FeriadoModel.DoesNotExist:
        feriados = None

    msgs = [f'Hoje é feriado de {f}' for f in feriados] if feriados else ['Hoje não éferiado']

    return render(request, 'feriados.html', {'msgs': msgs})