from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.UserCreate.as_view()),
    path('', views.apiOverview, name="apiOverview"),
    path('posts/', views.PostView, name="PostView"),
    path('posts/<str:pk>/', views.DetailView, name="DetailView"),
    path('create/', views.CreateView, name="CreateView"),
    path('update/<str:pk>/', views.UpdateView, name="UpdateView"),
    path('delete/<str:pk>/', views.DeleteView, name="DeleteView"),
]
