from django.db import models

# Create your models here.

class Doctors(models.Model):
   name = models.CharField(max_length=300) 
   email = models.EmailField(max_length=200)
   description = models.TextField(max_length=400) 
   image = models.ImageField(upload_to='doc/') 
   phone = models.CharField(max_length=12)
   def __str__(self):
       return self.name