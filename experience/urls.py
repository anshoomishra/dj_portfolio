from django.urls import path
from .views import ExperienceTemplateView
app_name = "experience"
urlpatterns = [
    path('',ExperienceTemplateView.as_view(),name="experience")
]