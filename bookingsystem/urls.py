from django.urls import include, path
from django.contrib import admin
from django.urls import path
from bookingsystem import views

urlpatterns = [
    path('', views.Home, name="home"),
    path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
    path("account/", include("users.urls")),
    path("employee/", include("employee.urls")),
    path("inventory/", include("inventory.urls")),
    path("external/", include("external.urls")),
    path("profile", views.ViewProfile, name="profile"),
    path("update-profile", views.UpdateProfile, name="update-profile"),
    path("book", views.StartBooking, name="book"),
    path("register-booking", views.RegisterBooking, name="register-booking"),
    path("my-bookings", views.UserBookingsList, name="user-bookings"),
    path("my-bookings/<bookingId>", views.BookingDetails, name="booking-details"),
    path("print-booking/<bookingId>", views.PrintBooking, name="print-booking"),
]
