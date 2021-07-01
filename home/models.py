from django.db import models
from Doctors.models import Doctors
# Create your models here.


class Patients(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200,primary_key=True)
    Doctor = models.ForeignKey(Doctors,on_delete=models.CASCADE)
    notes = models.TextField(max_length=500)
    def __str__(self):
        return self.name
