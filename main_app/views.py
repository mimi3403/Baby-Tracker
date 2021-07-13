from django.shortcuts import render
from django.http import HttpResponse 
from .models import Baby


# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def babies_index(request):
  babies = Baby.objects.all()
  return render(request, 'babies/index.html', {'babies' :babies}) # this is a context dictionary. 

def babies_detail(request, baby_id):
  baby = Baby.objects.get(id=baby_id)
  return render(request, 'babies/detail.html', {'baby' : baby})