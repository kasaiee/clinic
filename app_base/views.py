from django.shortcuts import render

from app_base.models import Appointment


def index(request):
    return render(request, 'index.html')


def services(request):
    return render(request, 'services.html')


def invoice(request, pk):
    appointment = Appointment.objects.get(pk=pk)
    ctx = {
        'appointment': appointment
    }
    return render(request, 'invoice.html', ctx)