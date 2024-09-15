from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Attendance, Employee
from .forms import CheckInForm, CheckOutForm
from django.utils.timezone import now

@login_required
def check_in(request):
    employee = Employee.objects.get(user=request.user)
    if request.method == 'POST':
        form = CheckInForm(request.POST)
        if form.is_valid():
            attendance = form.save(commit=False)
            attendance.employee = employee
            attendance.date = now().date()
            attendance.save()
            return redirect('attendance:dashboard')
    else:
        form = CheckInForm()
    return render(request, 'attendance/check_in.html', {'form': form})

@login_required
def check_out(request):
    employee = Employee.objects.get(user=request.user)
    attendance = Attendance.objects.filter(employee=employee, date=now().date()).first()
    if request.method == 'POST':
        form = CheckOutForm(request.POST, instance=attendance)
        if form.is_valid():
            form.save()
            return redirect('attendance:dashboard')
    else:
        form = CheckOutForm(instance=attendance)
    return render(request, 'attendance/check_out.html', {'form': form})

@login_required
def attendance_dashboard(request):
    employee = Employee.objects.get(user=request.user)
    records = Attendance.objects.filter(employee=employee).order_by('-date')
    return render(request, 'attendance/dashboard.html', {'records': records})

