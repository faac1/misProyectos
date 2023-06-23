from django import forms
from django.forms import ModelForm
from .models import Tipo_solicitud

class Tipo_solicitud_Form(ModelForm):
    class Meta:
        model = Tipo_solicitud
        fields = ["tipo_solicitud"]
        labels = {'tipo_solicitud':'Tipo solicitud'}