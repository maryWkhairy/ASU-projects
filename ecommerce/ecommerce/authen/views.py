from django.shortcuts import render, redirect
from .models import Register


# Create your views here.

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone_no = request.POST['phone_no']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        register = Register.objects.create(
            first_name=first_name,
            last_name=last_name,
            phone_no=phone_no,
            email=email,
            password=password
        )
        return redirect('home')
    else:
        return render(request, 'register.html')


def home(request):
    return render(request, 'home.html')
