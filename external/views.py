from django.shortcuts import render, redirect
from django.contrib.admin.views.decorators import staff_member_required, user_passes_test
from users.models import *
from employee.models import *
from django.contrib import messages
from datetime import datetime

@user_passes_test(lambda u: u.is_superuser)
def Reports(request):
    return render(request, "external/reports.html", {})

@user_passes_test(lambda u: u.is_superuser)
def EmployeeList(request):
    employeeProfiles = Profile.objects.filter(profileType="EMP")
    return render(request, "external/employeelist.html", {'employeeProfiles':employeeProfiles})

@user_passes_test(lambda u: u.is_superuser)
def EmployeeDetails(request, empId):
    employeeProfile = Address.objects.get(profileId=empId)
    if request.method == "POST":
        profileData = Profile.objects.get(id = empId)
        addressData = Address.objects.get(profileId = profileData.id)
        #update user email
        profileData.emailAddress = request.POST["email"]
        #update profile
        profileData.position = request.POST["position"]
        profileData.firstName = request.POST["firstName"]
        profileData.middleName = request.POST["middleName"]
        profileData.lastName = request.POST["lastName"]
        profileData.birthdate = request.POST["bday"]
        profileData.mobileNum = request.POST["contactNumber"]
        #update address
        addressData.streetAddress = request.POST["address"]
        addressData.city = request.POST["city"]
        addressData.province = request.POST["province"]
        addressData.country = request.POST["country"]
        addressData.zipcode = request.POST["zipCode"]
        profileData.save() #save changes
        addressData.save() #save changes
        messages.success(request, "Profile has been updated")
        return redirect("employee-details", empId)

    return render(request, "external/employeedetails.html",{'employeeProfile':employeeProfile})

@user_passes_test(lambda u: u.is_superuser)
def EmployeeAttendance(request, empId):
    employeeProfile = Address.objects.get(profileId=empId)
    attendanceData = EmployeeSignIn.objects.filter(profileId = empId)
    leaveData = EmployeeLeave.objects.filter(profileId = empId)
    return render(request, "external/employeeattendance.html",{'employeeProfile':employeeProfile, 'attendanceData':attendanceData, 'leaveData':leaveData})

@user_passes_test(lambda u: u.is_superuser)
def EmployeePayslip(request, empId):
    employeeSalaryList = EmployeeSalary.objects.filter(profileId = empId).order_by('date')
    employeeProfile = Address.objects.get(profileId=empId)
    return render(request, "external/employeepayslip.html",{'employeeProfile':employeeProfile, 'employeeSalaryList':employeeSalaryList})

def EmpLeaveAction(request, empId, leaveId):
    leaveData = EmployeeLeave.objects.get(id = leaveId)
    leaveData.status = request.POST['new-status']
    leaveData.adminNote = request.POST['admin-note']
    leaveData.save()
    messages.success(request, "Leave request has been updated")
    return redirect("employee-attendance", empId)

def SaveSalary(request, empId):
    EmployeeSalary.objects.create(
        profileId = Profile.objects.get(id=empId),
        ratePerHour= request.POST["ratePerHour"],
        hoursWorked= request.POST["hoursWorked"],
        bonus= request.POST["bonus"],
        adjustments= request.POST["adjustments"],
        totalSalary= (float(request.POST["ratePerHour"]) * float(request.POST["hoursWorked"])) - (float(request.POST["bonus"]) + float(request.POST["adjustments"])),
        date=  datetime.strptime(request.POST["salaryDate"], '%Y-%m').date()
    )
    messages.success(request, "Salary has been recorded")
    return redirect("employee-payslip", empId)

@staff_member_required
def BookingAdminView(request):
    if request.user.is_superuser:
        bookingsData = UserBookings.objects.all()
    else:
        empProfile = Profile.objects.get(userId=request.user.id)
        bookingsData = UserBookings.objects.filter(assignedEmployee=empProfile.id)
    return render(request, "external/bookingview.html", {"bookingsData":bookingsData})

@staff_member_required
def BookingAdminDetailsView(request, bookingId):
    bookingData = UserBookings.objects.get(id=bookingId)
    return render(request, "external/bookingdetailsview.html", {"bookingData":bookingData})

@staff_member_required
def BookingAction(request, bookingId):
    bookingData = UserBookings.objects.get(id=bookingId)
    bookingData.save()
    messages.success(request, f"Booking has been {request.POST['status']}")
    return redirect("booking-view")
