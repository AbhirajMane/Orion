from django.contrib import admin
from django.urls import include, path 
from home import views

urlpatterns = [
    path('',views.index, name='home'),
    path('about',views.about, name='about'),
    path('services',views.services, name='services'),
    path('contact',views.contact, name='contact'),
    path('geo.html',views.GeospatialSolutions, name='GeospatialSolutions'),
    path('civ.html',views.CivilandInfrastructure, name='Civil and Infrastructure'),
    path('sma.html',views.SmartCitySolutions, name='Smart City Solutions'),
    
]