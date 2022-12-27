from django.urls import path, include
from django.contrib import admin
from . import views


urlpatterns = [
     path('admin/', admin.site.urls),
     path('', views.Home.as_view(), name="home"),
     path('about/', views.About.as_view(), name="about"),
     path('cars/', views.Carslist.as_view(), name="cars_list")
]