import datetime

from django.test import TestCase
from django.urls import reverse

from .models import Inscription


class InscriptionListTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Crear 13 Inscripciones para probar la pagination
        number_of_inscriptions = 13
        for inscription_num in range(number_of_inscriptions):
            Inscription.objects.create(name='Nombre %s' % inscription_num, last_name='Apellidos %s' % inscription_num,
                                       address='Dirección %s' % inscription_num, country='Ciudad %s' % inscription_num,
                                       gender=0, postal_code=12345,
                                       dni=12345678901, birth_date=datetime.datetime.now(), phone=12345678,
                                       email='email@email%s.com' % inscription_num, average_time=1,
                                       email_confirm='email@email%s.com' % inscription_num, race_rules=True, )

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('inscription-list'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('inscription-list'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'inscription/list.html')

    # Ponerle el atributo paginate_by a la clase InscriptionList para que pasen las pruebas
    def test_pagination_is_ten(self):
        resp = self.client.get(reverse('inscription-list'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue(len(resp.context['object_list']) == 10)

    def test_lists_all_inscriptions(self):
        # Obtener 2da página y confirmar que tiene exactamente 3 elementos
        resp = self.client.get(reverse('inscription-list') + '?page=2')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue(len(resp.context['object_list']) == 3)
