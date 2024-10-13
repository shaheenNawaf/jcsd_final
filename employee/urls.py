from django.urls import include, path
from django.contrib import admin
from django.urls import path
from employee import views

urlpatterns = [
    path('attendance/', views.EmpAttendance, name="emp-attendance"),
    path('my-payslips/', views.EmpPayslips, name="emp-payslip"),
    
    
]
