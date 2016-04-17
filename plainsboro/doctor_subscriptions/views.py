from django.shortcuts import render
from django.contrib import messages
from django.template.defaultfilters import slugify
from plainsboro.doctor_subscriptions.forms import DoctorSubscribeForm
from plainsboro.doctor_subscriptions.models import Doctor


def doctor_subscribe(request):
    if request.method == 'POST':
        return subscribe(request)
    else:
        context = {'form': DoctorSubscribeForm()}
        return render(request,
                      'doctor_subscriptions/doctor_subscribe.html',
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
