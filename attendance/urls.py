from django.urls import path
from . import views

app_name = 'attendance'

urlpatterns = [
    path('check-in/', views.check_in, name='check_in'),
    path('check-out/', views.check_out, name='check_out'),
    path('dashboard/', views.attendance_dashboard, name='dashboard'),
]
