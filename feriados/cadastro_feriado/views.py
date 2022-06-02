from django.shortcuts import render

from .forms import FeriadoForm
from cadastro_api.models import FeriadoModel


def cadastra(request):
    if request.method == 'GET':
        return render(request, 'index.html', {'form': FeriadoForm()})

    if request.method == 'POST':
        form = FeriadoForm(request.POST)
        if form.is_valid():
            feriado = FeriadoModel(**form.cleaned_data)
            feriado.save()

            return render(request, 'ok.html', {'feriado': feriado})
