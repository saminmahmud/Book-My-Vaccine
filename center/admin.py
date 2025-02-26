from django.contrib import admin
from center.models import Center, Storage

class StorageInline(admin.TabularInline):
    model = Storage
    readonly_fields = ["booked_quantity"]

class CustomCenterAdmin(admin.ModelAdmin):
    inlines = [StorageInline]

admin.site.register(Center, CustomCenterAdmin)
