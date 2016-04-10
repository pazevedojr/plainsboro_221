from django.contrib import messages
from django.template.defaultfilters import slugify
from django.shortcuts import render
from plainsboro.core.forms import FindDoctorForm, DoctorSubscribeForm
from plainsboro.core.models import Doctor


def home(request):
    if request.method == 'POST':
        return create(request)
    else:
        context = {'form': FindDoctorForm()}
        return render(request, 'index.html', context)


def doctor_details(request, slug):
    context = {'doctor': Doctor(name='Dr. Hao123',
                                slug='hao123',
                                address='Rua Hao, 123',
                                phone='+55 11 123123123',
                                email='hao123@hao123.com')}
    return render(request, 'core/doctor_details.html', context)


def doctor_subscribe(request):
    if request.method == 'POST':
        return subscribe(request)
    else:
        context = {'form': DoctorSubscribeForm()}
        return render(request, 'core/doctor_subscribe.html', context)


def subscribe(request):
    form = DoctorSubscribeForm(request.POST)

    if not form.is_valid():
        messages.error(request, 'O formulário contem erros.')
        return render(request, 'core/doctor_subscribe.html', {'form': form})

    name = request.POST['name']
    slug = slugify(name)
    address = request.POST['address']
    neighborhood = request.POST['neighborhood']
    city = request.POST['city']
    phone = request.POST['phone']
    email = request.POST['email']
    specialization = request.POST['specialization']

    doctor = Doctor.objects.create(
        name=name, slug=slug, address=address, neighborhood=neighborhood,
        city=city, phone=phone, email=email, specialization=specialization
    )

    messages.success(request, 'Consultório cadastrado com sucesso!')

    context = {'form': DoctorSubscribeForm(),
               'doctor': doctor}

    return render(request, 'core/doctor_subscribe', context)


def create(request):
    form = FindDoctorForm(request.POST)

    if not form.is_valid():
        messages.error(request, 'O formulário contem erros.')
        return render(request, 'index.html', {'form': form})

    doctors = Doctor.objects.get(specialization=request.POST['specialization'],
                                 city=request.POST['city'])

    context = {'form': FindDoctorForm(),
               'doctors': doctors}

    return render(request, 'index.html', context)
