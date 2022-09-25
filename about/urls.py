from django.urls import path
from .views import AboutTemplate
app_name = "about"
urlpatterns = [
    path('',AboutTemplate.as_view(),name="about")
]