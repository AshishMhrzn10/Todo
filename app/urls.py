from django.urls import path
from . import views

urlpatterns = [
    path('', views.list, name="home"),
    path('add/', views.add_todo, name="add"),
]
