from http import HTTPStatus

from django.test import TestCase


class FeriadoFormTest(TestCase):
    def setUp(self):
        self.mockedData = {'nome': 'foo', 'data': '2022-04-02'}

    def test_post_sucesso(self):
        r = self.client.post('/cadastro/', data=self.mockedData)

        self.assertEqual(r.status_code, HTTPStatus.OK)
        self.assertContains(r, 'cadastrado com sucesso!')
