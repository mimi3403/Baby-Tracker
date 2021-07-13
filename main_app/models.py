from django.db import models

# Create your models here.
class Baby(models.Model):
  name = models.CharField(max_length=100)
  age = models.IntegerField()
  gender = models.CharField(max_length=100)
  personality = models.TextField(max_length=250)

  def __str__(self):
    return self.name