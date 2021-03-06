from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name="home"),
  path('about/', views.about, name="about"),
  path('babies/', views.babies_index, name="index"),
  path('babies/<int:baby_id>/change_diaper/',views.change_diaper, name='change_diaper'),
  path('babies/<int:baby_id>/assoc_toy/<int:toy_id>/', views.assoc_toy, name='assoc_toy'),
  path('babies/<int:baby_id>/remote_toy/<int:toy_id>/', views.remove_toy, name='remove_toy'),
  path('babies/<int:baby_id>/', views.babies_detail, name="detail"),
  path('babies/create/', views.BabyCreate.as_view(), name="babies_create"),
  path('babies/<int:pk>/update/', views.BabyUpdate.as_view(), name="babies_update"),
  path('babies/<int:pk>/delete/', views.BabyDelete.as_view(), name="babies_delete"),
  path('toys/', views.ToyList.as_view(), name='toys_index'),
  path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toys_detail'),
  path('toys/create/', views.ToyCreate.as_view(), name='toys_create'),
  path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name="toys_update"),
  path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name="toys_delete"),
  path('accounts/signup', views.signup, name="signup"),
]

