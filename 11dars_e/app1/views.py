from django.shortcuts import render
from django.views.generic import ListView
from .models import Post1
# Create your views here.
class HomePageView(ListView):
    model = Post1
    template_name = 'home.html'

class AboutPageView(ListView):
    template_name = 'about.html'