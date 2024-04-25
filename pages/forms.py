from django import forms
from django.forms import ModelForm
from .models import TeachingAssistant

class HoursForm(forms.ModelForm):
    class Meta:
        model = TeachingAssistant
        fields = '__all__'