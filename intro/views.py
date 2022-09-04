from django.shortcuts import render
from django.views.generic import TemplateView
from intro.models import Introduction
# Create your views here.

class HomePage(TemplateView):
    template_name = 'intro/intro.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['intro_data'] = Introduction.objects.all().first()
        return context
    