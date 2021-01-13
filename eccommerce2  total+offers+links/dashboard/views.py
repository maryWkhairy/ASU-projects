from django.shortcuts import render, redirect
from .models import Additem
from .forms import AdditemForm
from cart.models import Add_to_cart, Total_for_user


# Create your views here.

def dashboard(request):

    if request.method == 'POST':
        form = AdditemForm(request.POST, request.FILES)
        if form.is_valid():
            additem=form.save(commit=False)
            additem.user=request.user
            additem.save()
            items = Additem.objects.filter(user=request.user)
            return render(request, 'dashboard.html', {'form': form, 'items': items})

    else:
        form = AdditemForm()
        items = Additem.objects.filter(user=request.user)
        return render(request, 'dashboard.html', {'form': form, 'items': items})

def remove_item(request, pk):
    if request.method == 'POST':
        form = AdditemForm(request.POST, request.FILES)
        if form.is_valid():
            additem = form.save(commit=False)
            additem.user = request.user
            additem.save()
            items = Additem.objects.filter(user=request.user)
            return render(request, 'dashboard.html', {'form': form, 'items': items})

    else:
        #delete item from dashboard
        Additem.objects.filter(id=pk).delete()
        form = AdditemForm()
        items = Additem.objects.filter(user=request.user)

        #delete same item from cart
        Add_to_cart.objects.filter(product_id=pk).delete()
        Total_for_user.filter(product_id=pk, user=request.user).delete()
        return render(request, 'dashboard.html', {'form': form, 'items': items})