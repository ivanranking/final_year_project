from django.contrib import admin

from .models import Device, LeakEvent, SmsLog, UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "role", "updated_at")
    search_fields = ("user__username", "user__email", "role")
    readonly_fields = ("created_at", "updated_at")
    fieldsets = (
        ("User Information", {'fields': ('user',)}),
        ("Profile Details", {'fields': ('role', 'bio', 'profile_picture')}),
        ("Timestamps", {'fields': ('created_at', 'updated_at')}),
    )


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
