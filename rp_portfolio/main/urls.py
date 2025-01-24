from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),    
    path("home", views.home, name="home"),    
    path("aboutMe", views.home, name="aboutMe"),    
    path("education", views.home, name="education"),    
    path("contact", views.contact, name="contact"), 
    path("project/<int:id>/", views.project, name="project"),   
]
