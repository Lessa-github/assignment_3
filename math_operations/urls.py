 # Maps URLs to views for the math_operations app.
from django.urls import path
from . import views

urlpatterns = [
         path('', views.math_form_view, name='math_form'),
         path('result/', views.result_view, name='result'),
     ]
     