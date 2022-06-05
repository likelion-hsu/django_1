from django.shortcuts import render
from django.views.generic import TemplateView
#from .forms import PostForm


class index(TemplateView):
    template_name = 'index.html'
    
class first(TemplateView):
    template_name = 'first.html'
    
class second(TemplateView):
    template_name = 'second.html'
    
class third(TemplateView):
    template_name = 'third.html'
# Create your views here.
