from django.shortcuts import render
from django.contrib.auth import get_user_model

from .models import Stat, Task, UserTaskJunction, WTrack


User = get_user_model()


def index(request):
    users = User.objects.all().filter
    user_tasks = UserTaskJunction.objects.all()[:5]

    context = {
        'title': 'Users and Task',
        'users': users,
        'user_tasks': user_tasks,
    }

    return render(request, 'timeapp/index.html', context=context)


def start_work(request):
    context = {'title': "signup"}
    return render(request, 'timeapp/start_work.html', context=context)


class TaskDev:
    def __init__(self, task, user_list=[]):
        self.task = task
        self.user_list = user_list

    @property
    def get_task(self):
        return self.task

    @property
    def get_dev_list(self):
        return self.user_list


def stats(request):
    tasks = Task.objects.all()
    users = User.objects.all()
    user_tasks = UserTaskJunction.objects.all()

    data = []

    for task in tasks:
        data.append(TaskDev(task))

    for item in data:
        for user_task in user_tasks:
            if item.get_task.id == user_task.tid:
                item.get_dev_list.append(user_task.uid)

    for item in data:
        task, dev = item.get_task, item.user_list
        print(task, dev)

    context = {
        'title': "user stats",
        "data": []
    }

    return render(request, 'timeapp/stats.html', context=context)


def user_stats(request):
    context = {'title': "user stats"}
    return render(request, 'timeapp/stats.html', context=context)


def user_profile(request, id):
    user = User.objects.get(id=id)

    context = {
        'title': "Profile page",
        'user': user
    }

    if request.method == "POST":
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        # user.username = request.POST['username']

        user.save()

    return render(request, 'timeapp/user_profile.html', context=context)


# [
#     {
#         "task": id,
#         "devs": []
#     },
#     {
#         "task": id,
#         "devs": []
#     },
# ]


# TaskDev(1, [1, 2, 3])
