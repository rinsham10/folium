from django.urls import path 
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('templates/',
    views.template_selection,
    name='template_selection'),
    path('build/', views.build_portfolio, name='form_page'),
    path('submit/', views.submit_portfolio, name='submit_portfolio'),
     path('template1/', views.template1_view, name='template1'),
]