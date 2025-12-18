from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required

def is_admin(user):
    return user.is_staff

@staff_member_required
def home(request):
    return render(request, 'home.html')

@staff_member_required
def addproduct(request):
    return render(request, 'add.html')

@staff_member_required
def alterproduct(request):
    return render(request, 'alter.html')

@staff_member_required
def vieworder(request):
    return render(request, 'order.html')

@staff_member_required
def completedorder(request):
    return render(request, 'completed.html')