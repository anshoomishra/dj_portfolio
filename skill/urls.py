from .views import SkillTemplateView
from django.urls import path,include
app_name = "skill"
urlpatterns = [
    path('', SkillTemplateView.as_view(),name="skill-view"),
]