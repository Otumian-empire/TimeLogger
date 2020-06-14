from django.db import models
from django.contrib.auth.models import User

from django.utils import timezone

import datetime

# for the user class we are to use django's User
# we only need the username and password


class Task(models.Model):
    title = models.CharField("Task name", max_length=255, unique=True)
    description = models.TextField("Task description")

    def __str__(self):
        return self.title


class UserTaskJunction(models.Model):
    uid = models.ForeignKey(User, on_delete=models.CASCADE)
    tid = models.OneToOneField(Task, on_delete=models.CASCADE,  unique=True)

    def __str__(self):
        return f"{self.uid.username} - {self.tid.title}"


class WTrack(models.Model):
    uid = models.ForeignKey(User, on_delete=models.CASCADE)
    utjid = models.ForeignKey(UserTaskJunction, on_delete=models.CASCADE)
    timestart = models.DateTimeField(default=timezone.now)
    timeend = models.DateTimeField(blank=True, null=True,)
    # hours = models.FloatField()  # this is a derived attribute

    def __str__(self):
        return f"{self.uid.username} - {self.utjid.tid.title} - {self.timestart}"


class Stat(models.Model):
    wid = models.ForeignKey(WTrack, on_delete=models.CASCADE)
    number_of_weeks = models.IntegerField()
    total_hours = models.IntegerField()
    # average_hours = models.FloatField()  # this is a derived attribute
