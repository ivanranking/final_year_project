from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def login_view(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def dashboard(request):
    return render(request, 'dashboard.html')
 
def analytics(request):
    return render(request, 'analytics.html')

def reports(request):
    return render(request, 'reports.html')

def devices(request):
    return render(request, 'devices.html')

def sms_logs(request):
    return render(request, 'sms.html')

def admin_dashboard(request):
    return render(request, 'admin.html')