from django import forms

class FormRegistro(forms.Form):

    email=forms.EmailField()