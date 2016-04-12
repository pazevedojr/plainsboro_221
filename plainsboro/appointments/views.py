from django.shortcuts import render, get_object_or_404
from plainsboro.appointments.forms import MakeAppointmentForm
from plainsboro.core.models import Doctor


def doctor_details(request, slug):
    doctor = get_object_or_404(Doctor, slug=slug)

    if request.method == 'POST':
        return appointment(request, doctor)
    else:
        context = {'doctor': doctor,
                   'form': MakeAppointmentForm()}
        return render(request,
                      'appointments/doctor_details.html', context)


def appointment(request, doctor):
    from django.http import HttpResponse
    return HttpResponse('Serviço indisponível no momento.')
