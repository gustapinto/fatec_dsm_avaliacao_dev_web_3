from django.shortcuts import render, HttpResponse
from datetime import date
from django.shortcuts import render
from cadastro_api.models import FeriadoModel

def verificar(request):
    hoje = date.today()

    try:
        feriado = FeriadoModel.objects.get(data=hoje)
    except FeriadoModel.DoesNotExist:
        feriado = None

    mensagem = f'Hoje é {feriado}' if feriado else 'Hoje não é feriado'

    return render(request, 'feriados.html', {'mensagem': mensagem})