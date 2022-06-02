from django.forms import ModelForm

from cadastro_api.models import FeriadoModel


class FeriadoForm(ModelForm):
    class Meta:
        model = FeriadoModel
        fields = ['nome', 'data']
