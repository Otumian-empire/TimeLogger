from django.urls import path

from . import views

urlpatterns = [
    # reads all users and tasks
    path('', views.index, name='index'),
    path('startwork/', views.start_work, name='start_work'),
    path('taskstats/', views.stats, name='task_stats'),
    path('userstats/', views.user_stats, name='user_stats'),
    path('user/<id>/', views.user_profile, name='user_profile'),
]
