from django.shortcuts import render, redirect
from .models import Todo
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required(login_url='/accounts/login/')
def list(request):
    qs = Todo.objects.filter(user=request.user).order_by('-date')
    context = {
        'lists': qs
    }
    return render(request, 'app/home.html', context)

@login_required(login_url='/accounts/login/')
def add_todo(request):
    if request.method == "POST":
        note = request.POST["note"]
        create = Todo.objects.create(user=request.user, description=note)
        create.save()
        messages.success(request, "Created a note")
        return redirect('home')
    else:
        return render(request, 'app/home.html')
        
    return render(request, 'app/home.html')
