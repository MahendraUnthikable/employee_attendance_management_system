from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
import pytz

cur_time=pytz.timezone('Asia/Calcutta')

# Create your models here.
class EmployeeProfile(models.Model):

    # PERSONAL DATA
    employee_name = models.ForeignKey(User, on_delete=models.CASCADE)
    employeeid = models.CharField(('Employee ID Number'),max_length=10,null=True,blank=True)
    department =  models.CharField(max_length=125)
    role = models.CharField(max_length=125)
    employeetype = models.CharField(('Employee Type'),max_length=15,blank=False,null=True)
 
    created = models.DateTimeField(verbose_name=('Created'),auto_now_add=True,null=True)
    updated = models.DateTimeField(verbose_name=('Updated'),auto_now=True,null=True)

    def __str__(self) -> str:
        return self.employee_name
        
class EmployeeCheckIN(models.Model):
      employee_profile = models.ForeignKey(User, on_delete=models.CASCADE)
      check_in_time = models.DateTimeField(default = datetime.now, blank=True)

      def __str__(self) -> str:
         return self.check_in_time

class EmployeeCheckOut(models.Model):
      employee_profile = models.ForeignKey('EmployeeProfile', on_delete=models.CASCADE)
      check_out_time = models.DateTimeField(default = datetime.now, blank=True)
      attendance_status = models.CharField(('attendance_status'),max_length=125,null=True,blank=False)
      attendance_type = models.CharField(('attendance_type'),max_length=125,null=False,blank=False)

      
      def __str__(self) -> str:
        return self.employee_profile
      


    



