from django import forms
from django.db.models.fields import DateField, TimeField
from .models import Appoinment
from django.forms.widgets import SelectMultiple, TextInput, Textarea, EmailInput, CheckboxInput,URLInput, Select, NumberInput, RadioSelect, FileInput,DateInput,TimeInput


class AppoinmentForm(forms.ModelForm):
    class Meta:
        model = Appoinment
        exclude = ('timestamp',)
        widgets = {
            'name': TextInput(attrs={'class': 'required form-control', 'placeholder': 'Name'}),
            'phone': TextInput(attrs={'class': 'required form-control', 'placeholder': 'Phone'}),
            'date': DateInput(attrs={'class': 'required form-control', 'placeholder': 'Date','type':'date','id':'id_date'}),
            'time': Select(attrs={'class': 'required form-control', 'placeholder': 'Time'}),
        }
        