from django.urls import path
from .views import login_view

urlpatterns = [
    # path('signup/', SignupView.as_view()),
    path('login/', login_view, name="login"),
    # path('logout/', logout_view, name="logout")
]
