from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import AppointmentForm
from .models import Appointment

def home(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            ap = form.save()
            return redirect('booking:success', pk=ap.pk)
    else:
        form = AppointmentForm()
    stats = {'total': Appointment.objects.count(), 'today': Appointment.objects.count()}
    return render(request, 'booking/home.html', {'form': form, 'stats': stats})

def success(request, pk):
    ap = Appointment.objects.select_related('specialty').get(pk=pk)
    return render(request, 'booking/success.html', {'ap': ap})
