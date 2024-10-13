from django.urls import include, path
from django.contrib import admin
from django.urls import path
from external import views

urlpatterns = [
    path('reports', views.Reports, name="admin-reports"),
    path('employee-list', views.EmployeeList, name="employee-profiles"),
    path('employee-list/<empId>', views.EmployeeDetails, name="employee-details"),
    path('employee-list/attendance/<empId>', views.EmployeeAttendance, name="employee-attendance"),
    path('employee-list/payslip/<empId>', views.EmployeePayslip, name="employee-payslip"),
    path('employee-list/leave/<empId>/<leaveId>', views.EmpLeaveAction , name="emp-leave-action"),
    path('save-salary/<empId>', views.SaveSalary , name="save-salary"),
    path('bookings/view', views.BookingAdminView , name="booking-view"),
    path('bookings/view/<bookingId>', views.BookingAdminDetailsView , name="booking-details-view"),
    path('bookings/view/action/<bookingId>', views.BookingAction , name="booking-action"),
]
