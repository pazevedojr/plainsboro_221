from django.test import TestCase
from plainsboro.core.forms import FindDoctorForm


class FindDoctorsTest(TestCase):
    def setUp(self):
        self.response = self.client.get('')

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'index.html')

    def test_html(self):
        tags = (('<form', 1),
                ('<input', 4),
                ('type="text"', 2),
                ('type="submit"', 1))

        for tag, qtde in tags:
            with self.subTest():
                self.assertContains(self.response, tag, qtde)

    def test_csrf(self):
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_has_form(self):
        form = self.response.context['form']
        self.assertIsInstance(form, FindDoctorForm)

    def test_form_has_fields(self):
        form = self.response.context['form']
        fields = ['specialization', 'city']
        self.assertSequenceEqual(fields, list(form.fields))


class FindDoctorsMessageTest(TestCase):
    def test_error_message(self):
        data = dict(specialization='', city='')

        response = self.client.post('/', data, follow=True)
        self.assertContains(response, 'O formulário contem erros.')
