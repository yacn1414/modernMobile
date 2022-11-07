from dataclasses import field
from django import forms

class Emailc(forms.Form):
    Email = forms.CharField(label=False, max_length=50)
class contactForm(forms.Form):
    textmessage = forms.CharField(label=False, max_length=50)
