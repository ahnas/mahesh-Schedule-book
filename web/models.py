from django.db import models
from django.db.models.fields import DateField, SlugField
from versatileimagefield.fields import VersatileImageField
from tinymce.models import HTMLField
from django.urls import reverse

# Create your models here.

class Banner(models.Model):

    firstline = models.CharField(max_length=120)
    secondline = models.CharField(max_length=120)
    summary = models.CharField(max_length=120)
    photo = VersatileImageField('Photo',upload_to="Banner/")

    def __str__(self):
        return str(self.firstline)

class doctorAvailable(models.Model):
    day_CHOICES = (('Sunday', 'Sunday'),('Monday', 'Monday'),('Tuesday', 'Tuesday'),('Wednesday', 'Wednesday'),('Thursday', 'Thursday'),('Friday', 'Friday'),('Saturday', 'Saturday'))

    day = models.CharField(max_length=128,choices=day_CHOICES)
    fromTime = models.TimeField()
    toTime = models.TimeField()
    
        
    def __str__(self):
        return str(self.day)

class Appoinment(models.Model):

    
    name = models.CharField(max_length=120,)
    phone = models.CharField(max_length=120)
    date = DateField()
    time = models.CharField(max_length=128)

    def __str__(self):
        return str(self.name)

class Service(models.Model):
    name = models.CharField(max_length = 120)
    summary = models.CharField(max_length = 500)
    

    def __str__(self):
        return str(self.name)

class Award(models.Model):
    name = models.CharField(max_length=120)
    date = models.DateField()
    summary = models.CharField(max_length=120)
    photo = VersatileImageField('Photo',upload_to="Award/")

    def __str__(self):
        return str(self.name)

class Book(models.Model):
    name = models.CharField(max_length=120)
    photo = VersatileImageField('Photo',upload_to="Book/")

    def __str__(self):
        return str(self.name)

class Gallery(models.Model):
    photo = VersatileImageField('Photo',upload_to="Gallery/")

    def __str__(self):
        return str(self.photo)

class Update(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    date = models.DateField()
    photo = VersatileImageField('Photo',upload_to="Updates/")
    details = HTMLField()

    def get_absolute_url(self):
        return reverse ('web:updatesingle', kwargs={'slug':self.slug})

    def __str__(self):
        return str(self.name)


