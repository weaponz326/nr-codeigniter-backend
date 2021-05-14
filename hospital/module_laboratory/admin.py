from django.contrib import admin
from .models import Laboratory, Attachment


# Register your models here.

class LaboratoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'account', 'lab_code', 'lab_type', 'lab_date', 'patient')

class AttachmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'laboratory', 'attachment')

admin.site.register(Laboratory, LaboratoryAdmin)
admin.site.register(Attachment, AttachmentAdmin)
