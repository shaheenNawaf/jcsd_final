from django.urls import include, path
from django.contrib import admin
from django.urls import path
from inventory import views

urlpatterns = [
    path('', views.InventoryView, name="inventory"),
    path("supplier/", views.SupplierView, name="supplier"),
    path("delete-item/<itemId>", views.DeleteItem, name="delete-item"),
    path("delete-supplier/<suppId>", views.DeleteSupplier, name="delete-supplier"),
    path("edit-item/", views.EditItem, name="edit-item"),
    path("edit-supplier/", views.EditSupplier, name="edit-supplier"),
    
]
