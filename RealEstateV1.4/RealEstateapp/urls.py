from . import views
from django.urls import path

urlpatterns = [
    path('home', views.home, name="home"),
    path('contact', views.contact, name="contact"),
    path('happyclints', views.happyclients, name="happyclients"),
    path('newsandevent', views.newsandevent, name="newsandevent"),
    path('aboutus', views.aboutus, name="aboutus"),
    path('nricorner', views.nricorner, name='nricorner'),
    path('video', views.video, name="video"),
    path('ourproject', views.ourproject, name="ourproject"),
    path('ourprojectVenchar', views.ourprojectVenchar, name="ourprojectVenchar"),
   
    
]
