from django.urls import path
from . import views

app_name = 'web'

urlpatterns = [
    path('', views.index,name="index"), 
    path('profile/', views.profile,name="profile"),
    path('service/', views.service,name="service"),
    path('award/', views.award,name="award"),
    path('book/', views.book,name="book"),
    path('gallery/', views.gallery,name="gallery"),
    path('updates/', views.updates,name="updates"),
    path('contact/', views.contact,name="contact"),  
    path('appointment/', views.appointment,name="appointment"),
    path('updatesingle/<str:slug>', views.updatesingle,name="updatesingle"),
    path('dateday/', views.dateday,name="dateday"),
    
]