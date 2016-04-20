from django.test import TestCase
from plainsboro.doctor_subscriptions.forms import EditProfileForm
from plainsboro.doctor_subscriptions.models import Doctor


class EditDoctorProfileTest(TestCase):
    def setUp(self):
        self.doctor = Doctor.objects.create(
            name='Dr. Hao123',
            specialization='Oftalmologista',
            slug='hao123',
            address='Rua Hao, 123',
            city='Campinas',
            phone='+55 11 123123123',
            email='hao123@hao123.com')

        self.data = dict(
            name='Dr. Gregory House',
            address='Rua Princeton-Plainsboro, 221b',
            neighborhood='Plainsboro',
            city='Princeton',
            phone='+55 11 321321321',
            email='gregory@house.com.br',
            specialization='Medicina diagnóstica')

        self.response = self.client.get('/edit_profile/hao123/')

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.response,
                                'doctor_subscriptions/edit_profile.html')

    def test_html(self):
        pass

    def test_csrf(self):
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_has_form(self):
        form = self.response.context['form']
        self.assertIsInstance(form, EditProfileForm)

    def test_error_message(self):
        data = dict(name='', address='', neighborhood='', city='', phone='',
                    email='', specialization='')

        response = self.client.post('/edit_profile/hao123/', data, follow=True)
        self.assertContains(response, 'O formulário contem erros.')

    def test_success_message(self):
        response = self.client.post('/edit_profile/hao123/',
                                    self.data,
                                    follow=True)
        self.assertContains(response, 'Perfil atualizado com sucesso!')

    def test_edit_profile(self):
        self.client.post('/edit_profile/hao123/', self.data, follow=True)

        doctor = Doctor.objects.get(slug=self.doctor.slug)

        assert_list = [
            (self.data['name'], doctor.name),
            (self.data['address'], doctor.address),
            (self.data['neighborhood'], doctor.neighborhood),
            (self.data['city'], doctor.city),
            (self.data['phone'], doctor.phone),
            (self.data['email'], doctor.email),
            (self.data['specialization'], doctor.specialization),
        ]

        for attr, expected in assert_list:
            with self.subTest():
                self.assertEqual(attr, expected)
