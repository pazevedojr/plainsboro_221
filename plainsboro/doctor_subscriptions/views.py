from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.template.defaultfilters import slugify
from plainsboro.doctor_subscriptions.forms import DoctorSubscribeForm
from plainsboro.doctor_subscriptions.models import Doctor
from plainsboro.doctor_subscriptions.forms import EditProfileForm


def doctor_subscribe(request):
    if request.method == 'POST':
        return subscribe(request)
    else:
        context = {'form': DoctorSubscribeForm()}
        return render(request,
                      'doctor_subscriptions/doctor_subscribe.html',
                      context)


def doctor_profile(request, slug):
    doctor = get_object_or_404(Doctor, slug=slug)
    context = {'doctor': doctor}

    return render(request, 'doctor_subscriptions/doctor_profile.html', context)


def edit_profile(request, slug):
    doctor = get_object_or_404(Doctor, slug=slug)

    if request.method == 'POST':
        return edit(request, doctor)
    else:
        context = {'form': EditProfileForm()}
        return render(request,
                      'doctor_subscriptions/edit_profile.html',
                      context)


def subscribe(request):
    form = DoctorSubscribeForm(request.POST)

    if not form.is_valid():
        messages.error(request, 'O formulário contem erros.')
        return render(request,
                      'doctor_subscriptions/doctor_subscribe.html',
                      {'form': form})

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

    return render(request, 'core/doctor_subscribe.html', context)


def edit(request, doctor):
    form = EditProfileForm(request.POST)

    if not form.is_valid():
        messages.error(request, 'O formulário contem erros.')
        return render(request,
                      'doctor_subscriptions/edit_profile.html',
                      {'form': form})

    doctor.name = request.POST['name']
    doctor.address = request.POST['address']
    doctor.neighborhood = request.POST['neighborhood']
    doctor.city = request.POST['city']
    doctor.phone = request.POST['phone']
    doctor.email = request.POST['email']
    doctor.specialization = request.POST['specialization']
    doctor.save()

    messages.success(request, 'Perfil atualizado com sucesso!')

    context = {'form': EditProfileForm(),
               'doctor': doctor}

    return render(request,
                  'doctor_subscriptions/edit_profile.html',
                  context)
