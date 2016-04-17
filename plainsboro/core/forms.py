from django import forms


class FindDoctorForm(forms.Form):
    specialization = forms.CharField(label='Especialização')
    city = forms.CharField(label='Cidade')
