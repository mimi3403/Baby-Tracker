from django.shortcuts import render
from django.http import HttpResponse 

class Baby:
  def __init__(self, name, age, gender, personality):
    self.name = name
    self.age = age
    self.gender = gender
    self.personality = personality

babies = [
  Baby('Hannah', 0, 'female', 'lovely' ),
  Baby('Ryan', 2, 'male', 'aggresive' ),
  Baby('Emma', 3, 'female', 'eager to learn' ),
]


# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def babies_index(request):
  return render(request, 'babies/index.html', {'babies' :babies}) # this is a context dictionary