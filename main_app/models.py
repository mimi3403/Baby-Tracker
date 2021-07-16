from django.db import models
from django.urls import reverse
from datetime import date
# Create your models here.
CHANGING_TIMES = (
  ('M', 'Morning'),
  ('A', 'Afternoon'),
  ('E', 'Evening'),
)

class Toy(models.Model):
  name = models.CharField(max_length=100)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('toys_detail', kwargs={'pk': self.id})

class Baby(models.Model):
  name = models.CharField(max_length=100)
  age = models.IntegerField()
  gender = models.CharField(max_length=100)
  personality = models.TextField(max_length=250)

  toys = models.ManyToManyField(Toy)
  
  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse('detail', kwargs={'baby_id' : self.id })

  def changed_for_today(self):
    return self.diaper_set.filter(date=date.today()).count() >= len(CHANGING_TIMES)


class Diaper(models.Model):
  class Meta:
    ordering = ['-date']

  date = models.DateField('changing date')
  changing_time = models.CharField(
    max_length=1, 
    choices=CHANGING_TIMES, 
    default=CHANGING_TIMES[0][0]
  )

  baby = models.ForeignKey(Baby, on_delete=models.CASCADE)

  def __str__(self):
    return f'{self.get_changing_time_display()} on {self.date}'
