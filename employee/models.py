from django.db import models
from users.models import *
    
class EmployeeSignIn(models.Model):
    profileId = models.ForeignKey(Profile, on_delete=models.CASCADE)
    date = models.CharField(max_length=255)
    signInType = models.CharField(max_length=255)#clocked in or clocked out 

    def __str__(self):
        return f"{self.profileId.lastName}, {self.profileId.firstName} - {self.signInType} - {self.date}"
    
class EmployeeLeave(models.Model):
    profileId = models.ForeignKey(Profile, on_delete=models.CASCADE)
    leaveType = models.CharField(max_length=255)
    dateFrom = models.CharField(max_length=255)
    dateTo = models.CharField(max_length=255) 
    note = models.CharField(max_length=255, default="")
    adminNote = models.CharField(max_length=255, default="")
    status = models.CharField(max_length=255, default="Pending") 

    def __str__(self):
        return f"{self.profileId.lastName}, {self.profileId.firstName} - {self.leaveType} - {self.status}"


class EmployeeSalary(models.Model):
    profileId = models.ForeignKey(Profile, on_delete=models.CASCADE)
    ratePerHour  = models.CharField(max_length=255)
    hoursWorked = models.CharField(max_length=255)
    bonus = models.CharField(max_length=255)
    adjustments = models.CharField(max_length=255)
    totalSalary = models.CharField(max_length=255)
    date = models.DateField()

    def __str__(self):
        return f"{self.profileId.lastName} - {self.date}"
