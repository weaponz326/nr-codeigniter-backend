from django.contrib import admin
from .models import Folder, File


# Register your models here.

class FolderAdmin(admin.ModelAdmin):
    list_display = ('id', 'folder_name', 'folder_number', 'account', 'date_created')

class FileAdmin(admin.ModelAdmin):
    list_display = ('id', 'folder', 'file_name', 'file_number')

admin.site.register(Folder, FolderAdmin)
admin.site.register(File, FileAdmin)
