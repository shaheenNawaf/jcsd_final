from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from users.models import User, Profile, Address
from employee.views import clockInEmployee, clockOutEmployee

def LogIn(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return redirect("admin-reports")
        elif request.user.is_staff:
            return redirect("inventory")
    message = ""
    if request.method =="POST": #If user inputted login credentials
        user = authenticate(request,username=request.POST['username'],password=request.POST['password']) #authenticate user
        if user is not None: #if user exists
            login(request,user) #login user
            print(request.user.accessLevel)
            if request.user.is_staff and not request.user.is_superuser: #user.is_superuser
                clockInEmployee(request)
                messages.success(request, f'Hi Employee!')
                return redirect('inventory')
            elif request.user.is_superuser:
                messages.success(request, f'Hi Admin!')
                return redirect("admin-reports")
            else:
                messages.success(request, f'Log In Successfully')
            return redirect('home')
        else:
            messages.error(request, f'Invalid Username and Password or User does not exist')
    context = {'message' : message}
    return render(request,"users/login.html", context)

def SignUp(request):
    users = User.objects.all() #get all current users for crosschecking to prevent duplicate user credentials
    return render(request, "users/signup.html", {'users':users})

def LogoutAccount(request):
    if request.user.is_staff and not request.user.is_superuser: 
        clockOutEmployee(request)
    logout(request)
    messages.success(request, f'Log Out Successfully')
    return redirect('login')

def CreateAccount(request):
    User.objects.create_user( #add account to database
        username=request.POST['username'], 
        password=request.POST['password'], 
        email=request.POST['email'],
        ) #is_staff=True if user is employee
    createProfile(request) #create the account's profile
    registerAddress(request) #create the profile's address
    messages.success(request, "Account Created Successfully")
    return redirect("home")

def createProfile(request):
    newUser = User.objects.last() #fetch latest user created
    Profile.objects.create( #create profile for latest user
        userId = newUser,
        firstName = request.POST["firstName"],
        middleName = request.POST["middleName"],
        lastName = request.POST["lastName"],
        birthdate = request.POST["bday"],
        mobileNum = request.POST["contactNumber"],
        profileType = "USER"

    )

def registerAddress(request):
    newProfile = Profile.objects.last() #fetch latest user profile
    Address.objects.create( #create address for latest profile
        profileId = newProfile,
        streetAddress= request.POST["address"],
        city= request.POST["city"],
        province= request.POST["province"],
        country= request.POST["country"],
        zipcode= request.POST["zipCode"],
    )
