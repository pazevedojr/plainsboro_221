from django.test import TestCase
from plainsboro.core.forms import FindDoctorForm
from plainsboro.doctor_subscriptions.forms import DoctorSubscribeForm


class FindDoctorFormTest(TestCase):
    def test_form_has_fields(self):
        """ Form must have two fields """
        form = FindDoctorForm()
        expected = ['specialization', 'city']
        self.assertSequenceEqual(expected, list(form.fields))


class DoctorSubscribeFormTest(TestCase):
    def test_form_has_fields(self):
        """ Form must have seven fields """
        form = DoctorSubscribeForm()
        expected = ['name', 'address', 'neighborhood', 'city', 'phone',
                    'email', 'specialization']
        self.assertSequenceEqual(expected, list(form.fields))
