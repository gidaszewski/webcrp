from django import forms
from .models import *
from django.contrib.admin import widgets

class EmailForm(forms.Form):
    to_email = forms.EmailField(label='Destinatario')
    message = forms.CharField(widget=forms.Textarea, label='Mensaje')
