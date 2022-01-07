from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import json
from .forms import AppoinmentForm
from .models import Award, Banner, Book, Service,Gallery, Update


def index(request): 
    banner = Banner.objects.all()
    service = Service.objects.filter().order_by('-id')[:3]
    context = {
        "is_index" : True,
        "banner":banner,
        "service":service,
    }
    return render(request, 'index.html',context)

def profile(request):
    context = {
        "is_profile" : True
    }
    return render(request, 'profile.html',context) 

def service(request):
    service = Service.objects.all()
    context = {
        "is_service" : True,
        "service":service,
    }
    return render(request, 'service.html',context)


def award(request): 
    award = Award.objects.all()
    context = {
        "is_award" : True,
        "award" : award,
    }
    return render(request, 'award.html',context) 

def book(request):
    book = Book.objects.all()
    context = {
        "is_book" : True,
        "book":book,
    }
    return render(request, 'book.html',context)     


def gallery(request):
    gallery = Gallery.objects.all()
    context = {
        "is_gallery" : True,
        "gallery" : gallery,
    }
    return render(request, 'gallery.html',context)


def updates(request):
    update = Update.objects.all()
    context = {
        "is_updates" : True,
        "update":update,
    }
    return render(request, 'updates.html',context)

def updatesingle(request,slug):

    update = get_object_or_404(Update, slug = slug)
    context = {
        "is_updatesingle" : True,
        "update":update,
    }
    return render(request, 'updatesingle.html',context)


def contact(request): 
    context = {
        "is_contact" : True
    }
    return render(request, 'contact.html',context)

def appointment(request):
    appoinmentForm = AppoinmentForm(request.POST or None)
    if request.method == 'POST':
        if appoinmentForm.is_valid():
            appoinmentForm.save()
            response_data = {
                "status" : "true",
                "title" : "Successfully Booked",
                "message" : "Contact You Soon !"
            }
        else:
            response_data = {
                "status" : "false",
                "title" : "Form validation error",
            }
        return HttpResponse(json.dumps(response_data), content_type='application/javascript')
    else:
        context = {
            "is_appointment" : True,
            "appoinmentForm":appoinmentForm,
        }
    return render(request, 'appointment.html',context)