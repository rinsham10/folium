from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('templates/', views.template_selection, name='template_selection'),
    path('build/', views.build_portfolio, name='form_page'),
    path('submit/', views.submit_portfolio, name='submit_portfolio'),
    path('portfolio/<slug:slug>/', views.view_portfolio, name='view_portfolio'),
    path('portfolio/<slug:slug>/template2/', views.view_template2, name='view_template2'),  # Template 2
]
