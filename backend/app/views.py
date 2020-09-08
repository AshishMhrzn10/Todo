from django.shortcuts import render
from .models import Todo


def list(request):
    qs = Todo.objects.all().order_by('-date')
    context = {
        'lists': qs
    }
    return render(request, 'app/home.html', context)


def add_todo(request):
    pass
