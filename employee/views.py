from django.shortcuts import render, redirect
from employee.models import *
from datetime import datetime
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required, user_passes_test

@staff_member_required
def EmpAttendance(request):
    profileData = getProfileData(request.user.id)
    attendanceData = EmployeeSignIn.objects.filter(profileId = profileData.profileId.id).order_by("-id")
    leaveData = EmployeeLeave.objects.filter(profileId = profileData.profileId.id).order_by("-id")
    if request.method == "POST":
        registerLeaveForm(request)
        messages.success(request, "A request for Leave has been filed")
        return redirect("emp-attendance")
    return render(request, "employee/attendance.html",{'profileData':profileData, 'attendanceData':attendanceData, 'leaveData' :leaveData})


@user_passes_test(lambda u: u.is_superuser)
def Reports(request):
    return render(request, "admin/reports.html", {})

@staff_member_required
def EmpPayslips(request):
    empProfile = getProfileData(request.user.id)
    empId = empProfile.profileId.id
    employeeSalaryList = EmployeeSalary.objects.filter(profileId = empId).order_by('date')
    profileData = Address.objects.get(profileId=empId)

    return render(request, "employee/payslip.html", {'employeeSalaryList':employeeSalaryList, 'profileData':profileData})

def clockOutEmployee(request):
    profileData = getProfileData(request.user.id)
    date = datetime.now()
    EmployeeSignIn.objects.create(
        profileId = profileData.profileId,
        date = date.strftime("%d/%m/%Y %H:%M:%S"),
        signInType = "OUT",
    )

def clockInEmployee(request):
    profileData = getProfileData(request.user.id)
    date = datetime.now()
    EmployeeSignIn.objects.create(
        profileId = profileData.profileId,
        date = date.strftime("%d/%m/%Y %H:%M:%S"),
        signInType = "IN",
    )


def getProfileData(userId):
    profileData = Profile.objects.get(userId = userId)
    addressData = Address.objects.get(profileId = profileData.id)
    return addressData


def registerLeaveForm(request):
    EmployeeLeave.objects.create(
        profileId = Profile.objects.get(userId = request.user.id),
        leaveType = request.POST['leaveType'],
        dateFrom = request.POST['dateFrom'],
        dateTo = request.POST['dateTo'] ,
        note = request.POST['note'],
    )
