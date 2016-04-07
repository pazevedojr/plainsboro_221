from django.shortcuts import render
from plainsboro.core.forms import FindDoctorForm


def home(request):
    context = {'form': FindDoctorForm()}
    return render(request, 'index.html', context)
