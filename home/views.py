from django.shortcuts import render
from Doctors.models import Doctors
from .form import PatientForm

def main_page(request):
    doctor = Doctors.objects.all()
    if request.method == 'POST':
        form = PatientForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = PatientForm()
    return render(request, 'home.html',{'doctor':doctor,'form':form})
