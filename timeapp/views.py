from django.shortcuts import render
from django.contrib.auth import get_user_model

from .models import Stat, Task, UserTaskJunction, WTrack


User = get_user_model()


def index(request):
    users = User.objects.all().filter
    tasks = Task.objects.all()
    user_tasks = UserTaskJunction.objects.all()

    context = {
        'title': 'Users and Task',
        'users': users,
        'user_tasks': user_tasks,
    }

    return render(request, 'timeapp/index.html', context=context)


def start_work(request):
    context = {'title': "signup"}
    return render(request, 'timeapp/start_work.html', context=context)


def user_stats(request):
    context = {'title': "user stats"}
    return render(request, 'timeapp/stats.html', context=context)
