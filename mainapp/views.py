from django.shortcuts import render, redirect

from .forms import AppointmentForm


def new_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = AppointmentForm()
    return render(request, 'appointment_form.html', {'form': form})
