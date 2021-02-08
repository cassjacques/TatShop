from django import forms
from .models import Tats, Flash

class TatsForm(forms.ModelForm):
  class Meta:
    model = Tats
    fields = ['date', 'tat'] 

class FlashForm(forms.ModelForm):
  class Meta:
    model = Flash
    fields = [
      'description',
      'color',
    ]