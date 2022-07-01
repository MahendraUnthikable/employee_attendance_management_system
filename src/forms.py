from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import EmployeeProfile, EmployeeCheckIN, EmployeeCheckOut
from django import forms

class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=101)
    last_name = forms.CharField(max_length=101)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class EmployeeProfileForm(forms.ModelForm):
    class Meta:
        model = EmployeeProfile
        fields = "__all__"       


class EmployeeCheckInForm(forms.ModelForm):
    class Meta:
        model = EmployeeCheckIN
        fields = "__all__"                


class EmployeeAttendanceForm(forms.ModelForm):
    class Meta:
        model = EmployeeCheckOut
        fields = "__all__"                       