# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get_student/', views.get_student, name='get_student'),
]