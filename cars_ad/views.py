from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.shortcuts import render
from django.views import View 
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import Cars
# Create your views here.


class Home(TemplateView):
    template_name = "home.html"

class About(TemplateView):
    template_name = "about.html"

class Carslist(TemplateView):
    template_name = "cars_list.html"
      
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        make = self.request.GET.get("make")
        if make != None:
            context["cars"] = Cars.objects.filter(make__icontains=make)
        else:
            context["cars"] = Cars.objects.all()
        return context
   

   
class CarCreate(CreateView):
    model = Cars
    fields = ['make','year','model' ,'desc', 'img', 'price']
    template_name = "car_create.html"
    success_url = "/cars/"
      
class CarDetail(DetailView):
    model = Cars
    template_name = "car_detail.html"


class CarUpdate(UpdateView):
    model = Cars
    fields = ['make','year','model' ,'desc', 'img', 'price']
    template_name = "car_update.html"
    success_url = "/cars/"


class CarDelete(DeleteView):
    model = Cars
    template_name = "car_delete.html"
    success_url = "/cars/"