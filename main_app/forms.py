from django.forms import ModelForm, fields
from .models import Diaper

class DiaperForm(ModelForm):
  class Meta:
    model = Diaper
    fields = ['date', 'changing_time']