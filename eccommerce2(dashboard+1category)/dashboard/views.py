from django.shortcuts import render, redirect
from .models import Additem
from .forms import AdditemForm

# Create your views here.

def dashboard(request):
    ##user_name = request.user
    #current_user = request.user
    if request.method == 'POST':
        form = AdditemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            #user = Additem.objects.create(user=user_name)
            #user.save()
            #user = request.user
            ##user = Additem(user_name=user_name, user=request.user)
            ##user.save()
            items = Additem.objects.all()
            return render(request, 'dashboard.html', {'form': form, 'items': items})

    else:
        form = AdditemForm()
        items = Additem.objects.all()
        return render(request, 'dashboard.html', {'form': form, 'items': items})

def remove_item(request, pk):
    if request.method == 'POST':
        form = AdditemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            items = Additem.objects.all()
            return render(request, 'dashboard.html', {'form': form, 'items': items})

    else:
        Additem.objects.filter(id=pk).delete()
        form = AdditemForm()
        items = Additem.objects.all()
        return render(request, 'dashboard.html', {'form': form, 'items': items})