from os import error
from django.contrib.auth.models import User
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.shortcuts import redirect, render
from django.http import HttpResponse 
from .models import Baby, Toy
from .forms import DiaperForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid Signup Data - Please Try Again'
  form = UserCreationForm()
  return render(request, 'registration/signup.html', {'form': form, 'error_message': error_message})

@login_required
def babies_index(request):
  babies = Baby.objects.filter(user=request.user).order_by('age')
  return render(request, 'babies/index.html', {'babies' :babies}) # this is a context dictionary. 

@login_required
def change_diaper(request, baby_id):
  form = DiaperForm(request.POST)
  if form.is_valid():
    new_changing = form.save(commit=False)
    new_changing.baby_id = baby_id
    new_changing.save()
  return redirect('detail', baby_id=baby_id)

@login_required
def babies_detail(request, baby_id):
  baby = Baby.objects.get(id=baby_id)
  toys_babies_doesnt_have = Toy.objects.exclude(id__in = baby.toys.all().values_list('id'))
  diaper_form = DiaperForm()
  return render(request, 'babies/detail.html', {
    'baby' : baby, 
    'diaper_form' : diaper_form,
    'toys' : toys_babies_doesnt_have
  })

@login_required
def assoc_toy(request, baby_id, toy_id):
  Baby.objects.get(id=baby_id).toys.add(toy_id)
  return redirect('detail', baby_id=baby_id)

@login_required
def remove_toy(request, baby_id, toy_id):
  Baby.objects.get(id=baby_id).toys.remove(toy_id)
  return redirect('detail', baby_id=baby_id)

class BabyCreate(LoginRequiredMixin, CreateView):
  model = Baby
  fields = ['name', 'age', 'gender', 'personality']

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)


class BabyUpdate(LoginRequiredMixin, UpdateView):
  model = Baby
  fields = ['age', 'personality']

class BabyDelete(LoginRequiredMixin, DeleteView):
  model = Baby
  success_url = '/babies/'

class ToyList(LoginRequiredMixin, ListView):
  model = Toy

class ToyDetail(LoginRequiredMixin, DetailView):
  model = Toy

class ToyCreate(LoginRequiredMixin, CreateView):
  model = Toy
  fields = '__all__'

class ToyUpdate(LoginRequiredMixin, UpdateView):
  model = Toy
  fields = ['name']

class ToyDelete(LoginRequiredMixin, DeleteView):
  model = Toy
  success_url = '/toys/'