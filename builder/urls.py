from django.urls import path 
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('templates/',
    views.template_selection,
    name='template_selection'),
]