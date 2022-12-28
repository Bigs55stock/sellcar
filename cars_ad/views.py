from django.shortcuts import render
from django.views import View 
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import Cars
# Create your views here.



class Home(View):

   
    def get(self, request):
       return HttpResponse("Homepage")

class About(View):

    def get(self, request):
        return HttpResponse("About page")

class Carslist(View):

    def get(self, request):
        return HttpResponse("car page")


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
            context["cars"] = Cars.objects.filter(name__icontains=make)
        else:
            context["cars"] = Cars.objects.all()
        return context
   

   

      