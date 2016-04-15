from django.conf import settings
from django.core import mail
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string

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
    form = MakeAppointmentForm(request.POST)

    if not form.is_valid():
        return render(request,
                      'appointments/doctor_details.html',
                      {'form': form})

    class Appointment:
        def __init__(self, pacient_email, date, time):
            self.pacient_email = pacient_email
            self.date = date
            self.time = time

    pacient_appointment = Appointment(
        pacient_email=request.POST['email'],
        date=request.POST['date'],
        time=request.POST['time']
    )

    subject = 'Solicitação de agendamento de consulta'
    from_ = settings.DEFAULT_FROM_EMAIL
    to = [doctor.email, form.cleaned_data['email']]
    template = 'appointments/appointment_template.txt'
    context = {'appointment': pacient_appointment}

    _send_mail(subject,
               from_,
               to,
               template,
               context)

    messages.success(request, 'Sua solicitação de consulta foi realizada com '
                              'sucesso. Aguarde a confirmação do consultório '
                              'médico.')

    return HttpResponseRedirect('/doctors/{}/'.format(doctor.slug))


def _send_mail(subject, from_, to, template_name, context):
    body = render_to_string(template_name, context)
    mail.send_mail(subject, body, from_, to)