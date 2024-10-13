from django.shortcuts import render, redirect
from .models import * 
from django.contrib import messages

def InventoryView(request):
    inventoryData = Inventory.objects.all().order_by("-id")
    supplierData = Supplier.objects.all()
    if request.method == "POST":
        AddToInventory(request)
        messages.success(request, "Item has been added")
        return redirect("inventory")
    return render(request, "inventory/inventory.html", {'inventoryData':inventoryData, 'supplierData':supplierData})

def SupplierView(request):
    supplierData = Supplier.objects.all()
    if request.method == "POST":
        SaveSupplier(request)
        messages.success(request, "Supplier profile added")
        return redirect("supplier")
    return render(request, "inventory/supplier.html", {'supplierData':supplierData})

def AddToInventory(request):
    Inventory.objects.create(
        supplierId = Supplier.objects.get(id=request.POST['supplier']),
        itemName = request.POST['itemName'],
        itemType  = request.POST['itemType'],
        quantity = request.POST['quan'],
        price = request.POST['price'],
    )

def DeleteItem(request, itemId):
    data = Inventory.objects.get(id=itemId)
    data.delete()
    messages.success(request, "Item has been deleted")
    return redirect("inventory")

def EditItem(request):
    newSupplierData = Supplier.objects.get(name=request.POST['supplierId'])
    itemData = Inventory.objects.get(id=request.POST['item_id'])
    itemData.itemName = request.POST['itemName']
    itemData.itemType = request.POST['itemType']
    itemData.quantity = request.POST['quan']
    itemData.price = request.POST['price']
    itemData.supplierId = newSupplierData
    itemData.save()
    messages.success(request, "Item has been edited")
    return redirect("inventory")

def EditSupplier(request):
    supplierData = Supplier.objects.get(id=request.POST['supplier-id-edit'])
    supplierData.name= request.POST['name-edit']
    supplierData.address= request.POST['address-edit']
    supplierData.contactNum= request.POST['contactNum-edit']
    supplierData.email =request.POST['email-edit']
    supplierData.save()
    messages.success(request, "Supplier profile has been updated")
    return redirect("supplier")

def DeleteSupplier(request, suppId):
    data = Supplier.objects.get(id=suppId)
    data.delete()
    messages.success(request, "Supplier Profile has been deleted")
    return redirect("supplier")

def SaveSupplier(request):
    Supplier.objects.create(
        name= request.POST['name'],
        address= request.POST['address'],
        contactNum= request.POST['contactNum'],
        email = request.POST['email'],
    )