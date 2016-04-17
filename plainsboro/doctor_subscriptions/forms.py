from django import forms


class DoctorSubscribeForm(forms.Form):
    name = forms.CharField(label='Nome')
    address = forms.CharField(label='Endereço')
    neighborhood = forms.CharField(label='Bairro')
    city = forms.CharField(label='Cidade')
    phone = forms.CharField(label='Telefone')
    email = forms.CharField(label='Email')
    specialization = forms.CharField(label='Especialização')