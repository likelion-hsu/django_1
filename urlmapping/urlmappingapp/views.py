from django.views.generic import TemplateView

class Index(TemplateView):
    template_name = 'index.html'
    
class First(TemplateView):
    template_name = 'first.html'
    
class Second(TemplateView):
    template_name = 'second.html'
    
class Third(TemplateView):
    template_name = 'third.html'