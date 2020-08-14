from django.contrib import admin
from .models import Task

# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'task_name', 'priority', 'progress')

admin.site.register(Task, TaskAdmin)
