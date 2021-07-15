from django.contrib import admin

# Register your models here.
from .models import Baby, Toy, Diaper

admin.site.register(Baby)
admin.site.register(Toy)
admin.site.register(Diaper)
