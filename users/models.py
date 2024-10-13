from django.conf import settings
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _
from services.models import *

class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

class User(AbstractUser):
    """User model."""
    email = models.EmailField(unique=False)
    accessLevel = models.CharField(max_length=255, default="user")
    objects = UserManager()

class Profile(models.Model):
    class ProfileTypes(models.TextChoices):
            STEM = "EMP", _("employee")
            ABM = "USER", _("user")

    class EmployeePositions(models.TextChoices):
            TECHNICIAN = "TECH", _("Technician")
            JRTECHNICIAN = "JRTECH", _("Jr. Technician")
            SMM = "SMM", _("Social Media Manager")
            MM = "MM", _("Marketing Manager")

    userId = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, unique=True)
    firstName = models.CharField(max_length=255, null=True, blank=True)
    middleName = models.CharField(max_length=255, null=True, blank=True)
    lastName = models.CharField(max_length=255, null=True, blank=True)
    birthdate = models.CharField(max_length=255, null=True, blank=True)
    mobileNum = models.CharField(max_length=255, null=True, blank=True)
    profileType = models.CharField(max_length=100, choices=ProfileTypes.choices, default="USER")
    #FOR EMPLOYEE PROFILE
    emailAddress = models.CharField(max_length=255, null=True, blank=True)
    position = models.CharField(max_length=255, choices=EmployeePositions.choices, null=True, blank=True)
    employmentStatus = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.profileType} | {self.id} - {self.firstName} {self.middleName} {self.lastName}"

class Address(models.Model):
    profileId = models.ForeignKey(Profile, on_delete=models.CASCADE)
    streetAddress= models.CharField(max_length=255, null=True, blank=True)
    city= models.CharField(max_length=255, null=True, blank=True)
    province= models.CharField(max_length=255, null=True, blank=True)
    country= models.CharField(max_length=255, null=True, blank=True)
    zipcode= models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.profileId.lastName}'s Address"
    
class UserBookings(models.Model):
    userId = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, db_constraint=False)
    serviceId = models.ForeignKey(ServicesOffered, on_delete=models.CASCADE)
    locationId = models.ForeignKey(ServiceLocation, on_delete=models.CASCADE)
    date = models.CharField(max_length=255)
    time = models.CharField(max_length=255)
    status = models.CharField(max_length=255, default="Pending confirmation")
    assignedEmployee = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    #serviceFee
    #additionalFee
    #totalPrice
    #additional purchases
    #additional services

    def __str__(self):
        return f"{self.userId.username} - {self.date} || {self.time}" 

'''
class EmployeeAccount(models.Model):
    employeeId
    accessLevel
    CompanyRole
    EmployeeType
    isCommissionBased
'''

