from django.test import TestCase
from plainsboro.core.forms import DoctorSubscribeForm


class TestDoctorSubscribe(TestCase):
    def setUp(self):
        self.response = self.client.get('/doctor_subscribe/')

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'core/doctor_subscribe.html')

    def test_html(self):
        tags = (('<form', 1),
                ('<input', 9),
                ('type="text"', 7),
                ('type="submit"', 1))

        for tag, qtde in tags:
            with self.subTest():
                self.assertContains(self.response, tag, qtde)

    def test_csrf(self):
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_has_form(self):
        form = self.response.context['form']
        self.assertIsInstance(form, DoctorSubscribeForm)

    def test_form_has_fields(self):
        form = self.response.context['form']
        fields = ['name', 'address', 'neighborhood', 'city', 'phone',
                  'email', 'specialization']
        self.assertSequenceEqual(fields, list(form.fields))


class FindDoctorsMessage(TestCase):
    def test_error_message(self):
        data = dict(name='', address='', neighborhood='', city='', phone='',
                    email='', specialization='')

        response = self.client.post('/doctor_subscribe/', data, follow=True)
        self.assertContains(response, 'O formulário contem erros.')
