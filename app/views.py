from django.shortcuts import render
from .models import Todo
from django.contrib.auth.decorators import login_required


@login_required(login_url='/accounts/login/')
def list(request):
    qs = Todo.objects.all().order_by('-date')
    context = {
        'lists': qs
    }
    return render(request, 'app/home.html', context)


def add_todo(request):
    pass
