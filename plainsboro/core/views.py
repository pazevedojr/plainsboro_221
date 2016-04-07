from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages
from plainsboro.core.forms import FindDoctorForm


def home(request):
    if request.method == 'POST':
        return create(request)
    else:
        return new(request)


def create(request):
    form = FindDoctorForm(request.POST)

    if not form.is_valid():
        return render(request, 'index.html', {'form': form})

    messages.success(request, 'Procurando médicos na sua região...')

    return render(request, 'index.html', {'form': FindDoctorForm()})


def new(request):
    context = {'form': FindDoctorForm()}
    return render(request, 'index.html', context)
