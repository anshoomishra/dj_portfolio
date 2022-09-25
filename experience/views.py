from django.shortcuts import render
from django.views.generic import TemplateView
from experience.models import Company
# Create your views here.

class ExperienceTemplateView(TemplateView):
    template_name = "experience/experiences.html"
    
    def get_context_data(self,**kwargs):
        context = super(ExperienceTemplateView, self).get_context_data(**kwargs)
        context['companies'] = Company.objects.all()
        return context
