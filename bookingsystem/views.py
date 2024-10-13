from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from users.models import *
from services.models import *
from datetime import datetime, timedelta
from django.contrib.admin.views.decorators import staff_member_required, user_passes_test
from users.views import registerAddress, createProfile
#@staff_member_required use this if staff only view function
#@user_passes_test(lambda u: u.is_superuser) check if user is superuser if not redirect to log in page


def is_not_staff(user): #test function to determine if the current logged in user is staff or not
    return not user.is_staff

def Home(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return redirect("admin-reports")
        elif request.user.is_staff:
            return redirect("inventory")
    return render(request, "home.html", {})



@login_required
def ViewProfile(request):
    try:
        profileData = getProfileData(request.user.id)
    except:
        profileData = ""
    return render(request, "profile.html", {"profileData":profileData})

@user_passes_test(is_not_staff)
@login_required
def StartBooking(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return redirect("admin-reports")
        elif request.user.is_staff:
            return redirect("inventory")
    servicesData = ServicesOffered.objects.all()
    locationData = ServiceLocation.objects.all()
    bookingData = UserBookings.objects.all()
    profileData = getProfileData(request.user.id)
    return render(request, "book.html", {"servicesData":servicesData, "locationData": locationData, 'profileData':profileData, "bookingData":bookingData})

@login_required
def UpdateProfile(request):
    userData = User.objects.get(id = request.user.id)
    try:
        profileData = Profile.objects.get(userId = request.user.id)
        addressData = Address.objects.get(profileId = profileData.id)
        #update user email
        userData.email = request.POST["email"]
        profileData.emailAddress = request.POST["email"]
        #update profile
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
        userData.save() #save changes
        profileData.save() #save changes
        addressData.save() #save changes
    except:
        createProfile(request)
        registerAddress(request)
        userData.email = request.POST["email"]
        userData.save()
    messages.success(request, "Your Profile has been Updated")
    return redirect('profile')

@login_required
def RegisterBooking(request):
    profileData = User.objects.get(id=request.user.id)
    serviceData = ServicesOffered.objects.get(id=request.POST['serviceId']) 
    locationData = ServiceLocation.objects.get(id=request.POST['locationId'])
    UserBookings.objects.create( #create booking using form inputs
        userId = profileData,
        serviceId = serviceData,
        locationId = locationData,
        date = request.POST["date"],
        time = request.POST["time"],
    )
    messages.success(request, "Booking Saved. Please wait for the admin for confirmation")
    return redirect("user-bookings")

@login_required
def UserBookingsList(request):
    profileData = Profile.objects.get(userId = request.user.id)
    bookingsData = UserBookings.objects.filter(userId = request.user.id).order_by("-id")
    context={
        "bookingsData":bookingsData,
        "profileData":profileData
    }
    return render(request, "userbooking.html", context)

@login_required
def BookingDetails(request, bookingId):
    bookingDetails = UserBookings.objects.get(id=bookingId)
    profileData = getProfileData(request.user.id)
    return render(request, "bookingdetails.html",{"bookingDetails":bookingDetails, "profileData":profileData})

@login_required
def PrintBooking(request, bookingId):
    bookingDetails = UserBookings.objects.get(id=bookingId)
    profileData = getProfileData(request.user.id)
    return render(request, "printbooking.html",{"bookingDetails":bookingDetails, "profileData":profileData})


def getProfileData(userId):
    profileData = Profile.objects.get(userId = userId)
    addressData = Address.objects.get(profileId = profileData.id)
    return addressData
