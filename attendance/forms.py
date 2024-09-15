from django import forms
from .models import Attendance

class CheckInForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['check_in']

class CheckOutForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['check_out']
