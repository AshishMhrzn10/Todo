from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = 

    return render(request, 'accounts/login.html')
