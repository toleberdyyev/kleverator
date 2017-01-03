from django.shortcuts import render
from django.utils import timezone

from .models import Task

# Create your views here.

def task_list(request):
    tasks = Task.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

    data = {
        'tasks':tasks
    }
    return render(request, 'klvr/task_list.html', data)