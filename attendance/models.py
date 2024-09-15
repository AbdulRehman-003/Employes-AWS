from django.db import models

from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    employee_id = models.CharField(max_length=100, unique=True)
    department = models.CharField(max_length=100)
    position = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username

class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField(default=now)
    check_in = models.TimeField(null=True, blank=True)
    check_out = models.TimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.employee} - {self.date}'

    @property
    def hours_worked(self):
        if self.check_in and self.check_out:
            delta = datetime.combine(self.date, self.check_out) - datetime.combine(self.date, self.check_in)
            return delta.total_seconds() / 3600
        return 0

