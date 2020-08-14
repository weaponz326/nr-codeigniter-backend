from django.contrib import admin
from .models import Note, NoteFile

# Register your models here.

class NoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'subject', 'created_at', 'updated_at')

class NoteFileAdmin(admin.ModelAdmin):
    list_display = ('id', 'note', 'file')

admin.site.register(Note, NoteAdmin)
admin.site.register(NoteFile, NoteFileAdmin)
