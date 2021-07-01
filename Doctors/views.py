from django.shortcuts import render
from .models import Doctors

def doctors(request):
    doctor = Doctors.objects.all()
    return render(request, 'doctors.html', {'doctor':doctor})
# Create your views here.
