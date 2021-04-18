from django.contrib import admin
from .models import Worker


# Register your models here.

class WorkerAdmin(admin.ModelAdmin):
    list_display = ('id', 'account', 'first_name', 'last_name', 'worker_code', 'job')

admin.site.register(Worker, WorkerAdmin)
