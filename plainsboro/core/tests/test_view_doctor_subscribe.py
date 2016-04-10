from django.test import TestCase


class TestDoctorSubscribe(TestCase):
    def setUp(self):
        self.response = self.client.get('/doctor_subscribe/')

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'core/doctor_subscribe.html')
