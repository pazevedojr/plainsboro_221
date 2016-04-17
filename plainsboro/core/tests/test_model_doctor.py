from django.test import TestCase
from plainsboro.doctor_subscriptions.models import Doctor
from django.shortcuts import resolve_url as r


class DoctorModelTest(TestCase):
    def setUp(self):
        self.doctor = Doctor.objects.create(
            name='Dr. Hao123',
            slug='hao123',
            address='Rua Hao, 123',
            city='Campinas',
            phone='+55 11 123123123',
            email='hao123@hao123.com',
            specialization='Oftalmologista'
        )

    def test_create(self):
        self.assertTrue(Doctor.objects.exists())

    def test_str(self):
        self.assertEqual('Dr. Hao123', str(self.doctor))

    def test_get_absolute_url(self):
        url = r('doctor_details', slug=self.doctor.slug)
        self.assertEqual(url, self.doctor.get_absolute_url())
