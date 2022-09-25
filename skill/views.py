from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Skill
# Create your views here.


class SkillTemplateView(TemplateView):
    template_name = 'skill/skills.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['skills'] = Skill.objects.all()
        return context