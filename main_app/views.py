from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.shortcuts import redirect, render
from django.http import HttpResponse 
from .models import Baby, Toy
from .forms import DiaperForm


# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def babies_index(request):
  babies = Baby.objects.all().order_by('age')
  return render(request, 'babies/index.html', {'babies' :babies}) # this is a context dictionary. 

def change_diaper(request, baby_id):
  form = DiaperForm(request.POST)
  if form.is_valid():
    new_changing = form.save(commit=False)
    new_changing.baby_id = baby_id
    new_changing.save()
  return redirect('detail', baby_id=baby_id)

def babies_detail(request, baby_id):
  baby = Baby.objects.get(id=baby_id)
  toys_babies_doesnt_have = Toy.objects.exclude(id__in = baby.toys.all().values_list('id'))
  diaper_form = DiaperForm()
  return render(request, 'babies/detail.html', {
    'baby' : baby, 
    'diaper_form' : diaper_form,
    'toys' : toys_babies_doesnt_have
  })

def assoc_toy(request, baby_id, toy_id):
  Baby.objects.get(id=baby_id).toys.add(toy_id)
  return redirect('detail', baby_id=baby_id)

def remove_toy(request, baby_id, toy_id):
  Baby.objects.get(id=baby_id).toys.remove(toy_id)
  return redirect('detail', baby_id=baby_id)

class BabyCreate(CreateView):
  model = Baby
  fields = ['name', 'age', 'gender', 'personality']

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)


class BabyUpdate(UpdateView):
  model = Baby
  fields = ['age', 'personality']

class BabyDelete(DeleteView):
  model = Baby
  success_url = '/babies/'

class ToyList(ListView):
  model = Toy

class ToyDetail(DetailView):
  model = Toy

class ToyCreate(CreateView):
  model = Toy
  fields = '__all__'

class ToyUpdate(UpdateView):
  model = Toy
  fields = ['name']

class ToyDelete(DeleteView):
  model = Toy
  success_url = '/toys/'