from django.test import TestCase
from django.shortcuts import resolve_url as r
from plainsboro.core.models import Doctor


class DoctorDetailsTest(TestCase):
    def setUp(self):
        Doctor.objects.create(
            name='Dr. Hao123',
            specialization='Oftalmologista',
            slug='hao123',
            address='Rua Hao, 123',
            city='Campinas',
            phone='+55 11 123123123',
            email='hao123@hao123.com')
        self.response = self.client.get(r('doctor_details', slug='hao123'))

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'core/doctor_details.html')

    def test_html(self):
        contents = [
            'Dr. Hao123',
            'Oftalmologista',
            'Rua Hao, 123',
            'Campinas',
            '+55 11 123123123',
            'hao123@hao123.com'
        ]

        for expected in contents:
            with self.subTest():
                self.assertContains(self.response, expected)

    def test_context(self):
        doctor = self.response.context['doctor']
        self.assertIsInstance(doctor, Doctor)


class DoctorDetailsNotFoundTest(TestCase):
    def test_not_found(self):
        response = self.client.get(r('doctor_details', slug='not-found'))
        self.assertEqual(404, response.status_code)
