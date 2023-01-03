from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.shortcuts import redirect, render
from django.views import View 
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import Cars
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# Create your views here.


class Home(TemplateView):
    template_name = "home.html"

class About(TemplateView):
    template_name = "about.html"

@method_decorator(login_required, name='dispatch')
class Carslist(TemplateView):
    template_name = "cars_list.html"
      
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        make = self.request.GET.get("make")
        if make != None:
            context["cars"] = Cars.objects.filter(make__icontains=make, user=self.request.user)
        else:
            context["cars"] = Cars.objects.filter(user=self.request.user)
        return context
   
@method_decorator(login_required, name='dispatch')
class CarCreate(CreateView):
    model = Cars
    fields = ['make','year','model' ,'price', 'mileage','img','picture','picture1', 'desc','contact']
    template_name = "car_create.html"
    success_url = "/cars/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CarCreate, self).form_valid(form)


      
class CarDetail(DetailView):
    model = Cars
    template_name = "car_detail.html"


class CarUpdate(UpdateView):
    model = Cars
    fields = ['make','year','model' ,'price', 'mileage','img','picture','picture1', 'desc','contact']
    template_name = "car_update.html"
    success_url = "/cars/"


class CarDelete(DeleteView):
    model = Cars
    template_name = "car_delete.html"
    success_url = "/cars/"

class Signup(View):
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)
   
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("artist_list")
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)
