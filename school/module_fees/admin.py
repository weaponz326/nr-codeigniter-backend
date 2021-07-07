from django.contrib import admin
from .models import Fee, FeesItem, TargetClass, ArrearsItem, Bill


# Register your models here.

class FeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'account', 'fees_code', 'fees_date')

class TargetClassAdmin(admin.ModelAdmin):
    list_display = ('id', 'fee', 'clas')

class FeesItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'fee', 'item', 'amount')

class ArrearsItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'fee', 'item', 'source')

class BillAdmin(admin.ModelAdmin):
    list_display = ('id', 'fee', 'student', 'amount')

admin.site.register(Fee, FeeAdmin)
admin.site.register(TargetClass, TargetClassAdmin)
admin.site.register(FeesItem, FeesItemAdmin)
admin.site.register(ArrearsItem, ArrearsItemAdmin)
admin.site.register(Bill, BillAdmin)
