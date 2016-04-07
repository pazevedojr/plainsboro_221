from django.test import TestCase
from plainsboro.core.forms import FindDoctorForm


class FindDoctorsTests(TestCase):
    def setUp(self):
        self.response = self.client.get('')

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'index.html')

    def test_html(self):
        self.assertContains(self.response, '<form')
        self.assertContains(self.response, '<input', 4)
        self.assertContains(self.response, 'type="text"', 2)
        self.assertContains(self.response, 'type="submit"')

    def test_csrf(self):
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_has_form(self):
        form = self.response.context['form']
        self.assertIsInstance(form, FindDoctorForm)

    def test_form_has_fields(self):
        form = self.response.context['form']
        self.assertSequenceEqual(['specialization', 'city'], list(form.fields))