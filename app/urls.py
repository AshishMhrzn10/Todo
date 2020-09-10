from django.urls import path
from . import views

urlpatterns = [
    path('', views.list, name="home"),
    path('add/', views.add_todo, name="add"),
    path('update/<post_id>/', views.update_todo, name="update"),
    path('delete/<post_id>/', views.delete_todo, name="delete"),
]
