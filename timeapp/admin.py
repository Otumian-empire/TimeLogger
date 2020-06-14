from django.contrib import admin
from .models import Stat, Task, UserTaskJunction, WTrack

admin.site.register(Stat)
admin.site.register(Task)
admin.site.register(UserTaskJunction)
admin.site.register(WTrack)

