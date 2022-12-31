from django.urls import path
from . import views


urlpatterns = [
    
     path('', views.Home.as_view(), name="home"),
     path('about/', views.About.as_view(), name="about"),
     path('cars/', views.Carslist.as_view(), name="cars_list"),
     path('cars/new/', views.CarCreate.as_view(), name="car_create"),
]