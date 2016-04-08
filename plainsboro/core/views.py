from django.contrib import messages
from django.shortcuts import render
from plainsboro.core.forms import FindDoctorForm
from plainsboro.core.models import Doctor


def home(request):
    if request.method == 'POST':
        return create(request)
    else:
        return new(request)


def doctor_details(request, slug):
    context = {'doctor': Doctor(name='Dr. Hao123',
                                slug='hao123',
                                address='Rua Hao, 123',
                                phone='+55 11 123123123',
                                email='hao123@hao123.com')}
    return render(request, 'core/doctor_details.html', context)


def create(request):
    form = FindDoctorForm(request.POST)

    if not form.is_valid():
        messages.error(request, 'Desculpe. Algo errado aconteceu. Tente '
                                'novamente mais tarde.')
        return render(request, 'index.html', {'form': form})

    doctors = Doctor.objects.get(specialization=request.POST['specialization'],
                                 city=request.POST['city'])

    context = {'form': FindDoctorForm(),
               'doctors': doctors}
    return render(request, 'index.html', context)


def new(request):
    context = {'form': FindDoctorForm()}
    return render(request, 'index.html', context)
