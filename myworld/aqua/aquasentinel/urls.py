from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('analytics/', views.analytics, name='analytics'),
    path('reports/', views.reports, name='reports'),
    path('devices/', views.devices, name='devices'),
    path('sms/', views.sms_logs, name='sms'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
] 