from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),    
    path("home", views.home, name="home"),    
    path("about_me", views.aboutMe, name="aboutMe"),    
    path("education", views.education, name="education"),    
    path("projects", views.projects, name="projects"), 
    path("contact", views.contact, name="contact"), 
    path("project_view/<int:id>/", views.projects, name="project_view"),   
]
