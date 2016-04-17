from django.contrib import messages
from django.shortcuts import render
from plainsboro.core.forms import FindDoctorForm
from plainsboro.doctor_subscriptions.models import Doctor


def home(request):
    if request.method == 'POST':
        return create(request)
    else:
        context = {'form': FindDoctorForm()}
        return render(request, 'index.html', context)


def create(request):
    form = FindDoctorForm(request.POST)

    if not form.is_valid():
        messages.error(request, 'O formulário contem erros.')
        return render(request, 'index.html', {'form': form})

    doctors = Doctor.objects.all().filter(
        specialization=request.POST['specialization'],
        city=request.POST['city']
    )

    context = {'form': FindDoctorForm(),
               'doctors': doctors}

    return render(request, 'index.html', context)
