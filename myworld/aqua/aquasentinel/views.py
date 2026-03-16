from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import redirect, render

from .forms import ProfileForm
from .models import Device, LeakEvent


def index(request):
    return render(request, 'index.html')


def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()

    # Add small styling hints so the default Django form fields match the page styling.
    for field in form:
        field.field.widget.attrs.update({
            'class': 'form-control',
            'placeholder': field.label,
        })

    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('index')


def register(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Account created successfully. You are now logged in.")
            return redirect('dashboard')
        else:
            messages.error(request, "Please fix the errors below.")
    else:
        form = UserCreationForm()

    # Style the form fields to match existing design.
    for field in form:
        field.field.widget.attrs.update({
            'class': 'form-control',
            'placeholder': field.label,
        })

    return render(request, 'register.html', {'form': form})


@login_required(login_url='login')
def dashboard(request):
    devices = Device.objects.order_by('-updated_at')
    total_devices = devices.count()
    active_devices = devices.filter(is_active=True).count()

    latest_leak = LeakEvent.objects.order_by('-detected_at').first()
    recent_leaks = LeakEvent.objects.order_by('-detected_at')[:5]
    has_active_leak = LeakEvent.objects.filter(resolved=False).exists()

    context = {
        'total_devices': total_devices,
        'active_devices': active_devices,
        'latest_leak': latest_leak,
        'recent_leaks': recent_leaks,
        'has_active_leak': has_active_leak,
    }

    return render(request, 'dashboard.html', context)

@login_required(login_url='login')
def analytics(request):
    return render(request, 'analytics.html')

@login_required(login_url='login')
def reports(request):
    return render(request, 'reports.html')

@login_required(login_url='login')
def devices(request):
    devices = Device.objects.order_by('-updated_at')
    total_devices = devices.count()
    active_devices = devices.filter(is_active=True).count()
    inactive_devices = total_devices - active_devices

    context = {
        'devices': devices,
        'total_devices': total_devices,
        'active_devices': active_devices,
        'inactive_devices': inactive_devices,
    }

    return render(request, 'devices.html', context)

@login_required(login_url='login')
def sms_logs(request):
    return render(request, 'sms.html')


@login_required(login_url='login')
def admin_dashboard(request):
    return render(request, 'admin.html')