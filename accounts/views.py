from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password'] 
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Succesfully logged in!!!. Welcome {user.username},")
            return redirect('home')
        else:
            messages.error(request, "Invalid credentials")
            return redirect('login')
    return render(request, 'accounts/login.html')


def logout_view(request):
    logout(request)
    messages.success(request, "Succesfully logged out.")
    return redirect('login')


def signup_view(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        try:
            match1 = User.objects.filter(username=username).exists()
            match2 = User.objects.filter(email=email).exists()
            if match1:
                messages.error(request, "Username already exists")
                return redirect('signup')
            elif match2:
                messages.error(request, "Email already exists")
                return redirect('signup')
            else:
                if password != password2:
                    messages.error(request, "Password does not match.")
                    return redirect('signup')
                else:
                    user = User.objects.create_user(username=username, email=email, password=password)
                    user.save()
                    messages.success(request, "Signed up successfully. Please login.")
                    return redirect('login')
        except:
            return render(request, 'accounts/signup.html')


    return render(request, 'accounts/signup.html')
