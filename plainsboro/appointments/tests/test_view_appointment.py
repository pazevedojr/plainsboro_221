import datetime

from django.core import mail
from django.test import TestCase
from plainsboro.doctor_subscriptions.models import Doctor


class MakeAppointmentTest(TestCase):
    def setUp(self):
        Doctor.objects.create(
            name='Dr. Hao123',
            slug='hao123',
            address='Rua Hao, 123',
            city='Campinas',
            phone='+55 11 123123123',
            email='hao123@hao123.com',
            specialization='Oftalmologista'
        )

        data = dict(email='vinicius.ribeiro1@gmail.com',
                    date=datetime.date.today(),
                    time='12:00')

        self.response = self.client.post('/doctors/hao123/', data, follow=True)

    def test_post(self):
        self.assertRedirects(self.response, '/doctors/hao123/')

    def test_send_mail(self):
        self.assertEqual(1, len(mail.outbox))

    def test_success_message(self):
        self.assertContains(self.response, 'Sua solicitação de consulta foi '
                                           'realizada com sucesso. Aguarde a '
                                           'confirmação do consultório médico.')
