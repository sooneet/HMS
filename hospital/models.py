from operator import mod
from unicodedata import name
from django.db import models

# Create your models here.

class Doctor(models.Model):
    name = models.CharField(max_length=50)
    mobile = models.IntegerField()
    special = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Patient(models.Model):
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    mobile = models.IntegerField()
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE) 
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE)
    date1 = models.DateField()
    time1 = models.TimeField()

    def __str__(self):
        return self.doctor.name +"--"+ self.patient.name

class Contact(models.Model):
    name = models.CharField(max_length=50)
    mob_no = models.IntegerField() 
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=250)
    message_date = models.DateField()
    is_read = models.CharField(max_length=10,null=True)

    def __str__(self):
        return self.id

