from unicodedata import name
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import UserRegistrationForm, EmployeeProfileForm, EmployeeCheckInForm, EmployeeAttendanceForm
from datetime import datetime
from .models import EmployeeCheckIN, EmployeeCheckOut
from django.db.models import Q
import datetime
import logging

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def home(request):
    return render(request, './home.html')

def register(request):
    if request.method == 'POST':
        form = EmployeeProfileForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created. You can log in now!')    
            return redirect('home')
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, './register.html', context)


def employee_profile(request):
    if request.method == 'POST':
        user=request.user
        if not request.user.is_authenticated:
            return redirect('login')
        if not user:
            return redirect('login')
        form = EmployeeProfileForm(request.POST)
        if form.is_valid():
            form.save()
            logger.info("employee profile has been updated!")
            messages.success(request, f'Your account info has been saved!')    
            return redirect('home')
    else:
        form = EmployeeProfileForm()
    context = {'form': form}
    return render(request, './emp_profile.html', context)


def checkin(request):
    if request.method == 'POST':
        user=request.user
        if not request.user.is_authenticated:
            return redirect('login')
        form = EmployeeCheckInForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Employee checked-in successfully')    
            return redirect('home')
    else:
        form = EmployeeCheckInForm()
    context = {'form': form}
    return render(request, './check_in.html', context)


def checkout(request):
    if request.method == 'POST':
        user=request.user
        if not request.user.is_authenticated:
            return redirect('login')
        check_in_time=EmployeeCheckIN.objects.all().filter(employee_profile = request.user)
        print(check_in_time)
        check_out_time = datetime.datetime.now()
        """
        att_status = ['marked' , 'unmarked'] 
        att_type = ['absent', 'present', 'first_half' , 'second_half', 'half_day']
        check_in_time = "18:20"
        check_out_time="09:23"
        
        if check_out_time-check_in_time==9:
            attedance_status=att_status["marked"]
            attedance_type=att_type["present"]
            return data.save(update_fields=[attedance_status,attedance_type])   
        elif check_in_time >= 11:
            attedance_status=att_status["marked"]
            attedance_type=att_type["half_day"]
            return data.save(update_fields=[attedance_status,attedance_type])   
        elif check_out_time=<2:
            attedance_status=att_status["marked"]
            attedance_type=att_type["first_day"]
            return data.save(update_fields=[attedance_status,attedance_type])
        elif checkintime>= 2:
            attedance_status=att_status["marked"]
            attedance_type=att_type["second_day"]
            return data.save(update_fields=[attedance_status,attedance_type])
        else:
            attedance_status=att_status["unmarked"]
            attedance_type=att_type["absent"]
            return data.save(update_fields=[attedance_status,attedance_type])    
        """
    return render(request, './check_out.html')











