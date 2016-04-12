import datetime
from django import forms


class MakeAppointmentForm(forms.Form):
    email = forms.EmailField(label='Email')
    date = forms.DateField(label='Data', initial=datetime.date.today)
    time = forms.TimeField(label='Horário')
