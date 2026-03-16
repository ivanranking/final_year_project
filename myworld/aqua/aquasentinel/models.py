from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone


User = get_user_model()


class Device(models.Model):
    """A physical device that reports water flow / leak data."""

    name = models.CharField(max_length=120)
    serial_number = models.CharField(max_length=120, unique=True)
    location = models.CharField(max_length=255, blank=True)
    is_active = models.BooleanField(default=True)
    last_seen = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-updated_at"]

    def __str__(self):
        return f"{self.name} ({self.serial_number})"


class LeakEvent(models.Model):
    """Represents a detected leak event from a device."""

    SEVERITY_CHOICES = [
        ("low", "Low"),
        ("medium", "Medium"),
        ("high", "High"),
    ]

    device = models.ForeignKey(Device, on_delete=models.CASCADE, related_name="leak_events")
    detected_at = models.DateTimeField(default=timezone.now)
    severity = models.CharField(max_length=10, choices=SEVERITY_CHOICES, default="low")
    description = models.TextField(blank=True)
    resolved = models.BooleanField(default=False)
    resolved_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ["-detected_at"]

    def __str__(self):
        return f"Leak on {self.device.name} @ {self.detected_at:%Y-%m-%d %H:%M}"


class SmsLog(models.Model):
    """Record of SMS alerts sent through the system."""

    sent_at = models.DateTimeField(default=timezone.now)
    to_number = models.CharField(max_length=30)
    message = models.TextField()
    success = models.BooleanField(default=False)
    response = models.TextField(blank=True)

    class Meta:
        ordering = ["-sent_at"]

    def __str__(self):
        return f"SMS to {self.to_number} @ {self.sent_at:%Y-%m-%d %H:%M} ({'OK' if self.success else 'FAIL'})"
 