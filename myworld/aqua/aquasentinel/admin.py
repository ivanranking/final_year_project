from django.contrib import admin

from .models import Device, LeakEvent, SmsLog


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ("name", "serial_number", "location", "is_active", "last_seen", "updated_at")
    list_filter = ("is_active",)
    search_fields = ("name", "serial_number", "location")


@admin.register(LeakEvent)
class LeakEventAdmin(admin.ModelAdmin):
    list_display = ("device", "detected_at", "severity", "resolved")
    list_filter = ("severity", "resolved")
    search_fields = ("device__name", "description")
    raw_id_fields = ("device",)


@admin.register(SmsLog)
class SmsLogAdmin(admin.ModelAdmin):
    list_display = ("to_number", "sent_at", "success")
    list_filter = ("success",)
    search_fields = ("to_number", "message")
