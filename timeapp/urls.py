from django.urls import path

from . import views

urlpatterns = [
    # reads all users and tasks
    path('', views.index, name='index'),
    path('startwork/', views.start_work, name='start_work'),
    path('userstats/', views.user_stats, name='user_stats'),
]
