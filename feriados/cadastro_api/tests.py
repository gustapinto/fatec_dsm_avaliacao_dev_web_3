from datetime import datetime

from django.test import TestCase

from .models import FeriadoModel
from .utils.FeriadosAPI import FeriadoAPI


class FeriadoModelTest(TestCase):
    def setUp(self):
        self.feriado = 'Natal'
        self.data = datetime.strptime('2022-12-25','%Y-%m-%d').date()

        self.feriado_cadastrado = FeriadoModel(nome=self.feriado, data=self.data)
        self.feriado_cadastrado.save()

    def test_feriado_criado(self):
        self.assertTrue(FeriadoModel.objects.exists())

    def test_feriado_nome(self):
        self.assertEqual(self.feriado_cadastrado.nome, self.feriado)

    def test_feriado_data(self):
        self.assertEqual(self.feriado_cadastrado.data, self.data)


class FeriadoApiTest(TestCase):
    def test_instanciar_objeto(self):
        objeto = FeriadoAPI(2022)
        assert objeto._ano, 2022
        assert type(objeto.feriados) == list
        assert len(objeto.feriados) == 11

    def test_str_repr(self):
        objeto = FeriadoAPI(2023)
        msg = 'Feriados de 2023'
        assert str(objeto) == msg
        assert repr(objeto) == msg

    def test_str_repr2(self):
        objeto = FeriadoAPI(2022)
        msg = 'Feriados de 2022'
        assert str(objeto) == msg
        assert repr(objeto) == msg

    def test_properties(self):
        objeto = FeriadoAPI(2022)
        assert objeto.ano == '2022'
