from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name="home"),
  path('about/', views.about, name="about"),
  path('babies/', views.babies_index, name="index"),
  path('babies/<int:baby_id>/', views.babies_detail, name="detail"),
  path('babies/create/', views.BabyCreate.as_view(), name="babies_create"),
]

