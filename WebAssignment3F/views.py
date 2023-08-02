from django.shortcuts import render
from django.db import connection

def contactUsForm(request):
    return render(request, "contactUs.html")

def saveData(request):
    if request.method=="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        message = request.POST.get('message')

        cursor=connection.cursor()
        query = f"INSERT INTO contactformdb.contactusform_contactformdata (name, email, phone, address, message) VALUES ('{name}', '{email}', '{phone}', '{address}', '{message}')"
        cursor.execute(query)
    
    return render(request, "contactUs.html")