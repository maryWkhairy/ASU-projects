from django.shortcuts import render, redirect
from dashboard.models import Additem
from .models import Whishlist
from django.contrib.auth.models import User
from reg.models import type_of_customer
# Create your views here.
def home(request):
    return render(request, 'home.html')


def reg(request):
    return render(request, 'reg.html')


def log(request):
    return render(request, 'log.html')

def buyer(request):
    return render(request,'buyer_homepage.html')

def seller(request):
    return render(request,'seller_homepage.html')


# Categories
def chairs(request):
    if request.method == 'POST':
        h = User.objects.filter(username=request.user).exists()
        print(h)
        if h:
            t = type_of_customer.objects.filter(username=request.user).values_list('type',flat=True).get(username=request.user)
            print(t)
            if t == 'Buyer':
                return redirect('/buyer')
            elif t == 'seller':
                return redirect('/seller')
            else:
                return redirect('/home')
    chairs = Additem.objects.filter(category='chairs')
    return render(request, 'chairs.html', {'chairs': chairs})


def armchairs(request):
    if request.method == 'POST':
        h = User.objects.filter(username=request.user).exists()
        print(h)
        if h:
            t = type_of_customer.objects.filter(username=request.user).values_list('type',flat=True).get(username=request.user)
            print(t)
            if t == 'Buyer':
                return redirect('/buyer')
            elif t == 'seller':
                return redirect('/seller')
            else:
                return redirect('/home')
    armchairs = Additem.objects.filter(category='armchairs')
    return render(request, 'armchairs.html', {'armchairs': armchairs})


def chaiselongues(request):
    if request.method == 'POST':
        h = User.objects.filter(username=request.user).exists()
        print(h)
        if h:
            t = type_of_customer.objects.filter(username=request.user).values_list('type',flat=True).get(username=request.user)
            print(t)
            if t == 'Buyer':
                return redirect('/buyer')
            elif t == 'seller':
                return redirect('/seller')
            else:
                return redirect('/home')
    chaiselongues = Additem.objects.filter(category='chaiselongues')
    return render(request, 'chaiselongues.html', {'chaiselongues': chaiselongues})


def sofas(request):
    if request.method == 'POST':
        h = User.objects.filter(username=request.user).exists()
        print(h)
        if h:
            t = type_of_customer.objects.filter(username=request.user).values_list('type',flat=True).get(username=request.user)
            print(t)
            if t == 'Buyer':
                return redirect('/buyer')
            elif t == 'seller':
                return redirect('/seller')
            else:
                return redirect('/home')
    sofas = Additem.objects.filter(category='sofas')
    return render(request, 'sofas.html', {'sofas': sofas})


def wardrobes(request):
    if request.method == 'POST':
        h = User.objects.filter(username=request.user).exists()
        print(h)
        if h:
            t = type_of_customer.objects.filter(username=request.user).values_list('type',flat=True).get(username=request.user)
            print(t)
            if t == 'Buyer':
                return redirect('/buyer')
            elif t == 'seller':
                return redirect('/seller')
            else:
                return redirect('/home')
    wardrobes = Additem.objects.filter(category='wardrobes')
    return render(request, 'wardrobes.html', {'wardrobes': wardrobes})


def beds(request):
    if request.method == 'POST':
        h = User.objects.filter(username=request.user).exists()
        print(h)
        if h:
            t = type_of_customer.objects.filter(username=request.user).values_list('type',flat=True).get(username=request.user)
            print(t)
            if t == 'Buyer':
                return redirect('/buyer')
            elif t == 'seller':
                return redirect('/seller')
            else:
                return redirect('/home')
    beds = Additem.objects.filter(category='beds')
    return render(request, 'beds.html', {'beds': beds})


def shelving_units(request):
    if request.method == 'POST':
        h = User.objects.filter(username=request.user).exists()
        print(h)
        if h:
            t = type_of_customer.objects.filter(username=request.user).values_list('type',flat=True).get(username=request.user)
            print(t)
            if t == 'Buyer':
                return redirect('/buyer')
            elif t == 'seller':
                return redirect('/seller')
            else:
                return redirect('/home')
    shelving_units = Additem.objects.filter(category='shelving units')
    return render(request, 'shelving_units.html', {'shelving_units': shelving_units})


def tables(request):
    if request.method == 'POST':
        h = User.objects.filter(username=request.user).exists()
        print(h)
        if h:
            t = type_of_customer.objects.filter(username=request.user).values_list('type',flat=True).get(username=request.user)
            print(t)
            if t == 'Buyer':
                return redirect('/buyer')
            elif t == 'seller':
                return redirect('/seller')
            else:
                return redirect('/home')
    tables = Additem.objects.filter(category='tables')
    return render(request, 'tables.html', {'tables': tables})




# whishlist

def Chairs(request, pk):
    image = Additem.objects.values_list('image', flat=True).get(id=pk)
    description = Additem.objects.values_list('description', flat=True).get(id=pk)
    price = Additem.objects.values_list('price', flat=True).get(id=pk)
    user = request.user
    if (Whishlist.objects.filter(old_id=pk).exists()) == False:
        new_item = Whishlist.objects.create(image=image, description=description, price=price, user=user, old_id=pk)
    return redirect('chairs')


def Armchairs(request, pk):
    image = Additem.objects.values_list('image', flat=True).get(id=pk)
    description = Additem.objects.values_list('description', flat=True).get(id=pk)
    price = Additem.objects.values_list('price', flat=True).get(id=pk)
    user = request.user
    if (Whishlist.objects.filter(old_id=pk).exists()) == False:
        new_item = Whishlist.objects.create(image=image, description=description, price=price, user=user, old_id=pk)
    return redirect('armchairs')


def Sofas(request, pk):
    image = Additem.objects.values_list('image', flat=True).get(id=pk)
    description = Additem.objects.values_list('description', flat=True).get(id=pk)
    price = Additem.objects.values_list('price', flat=True).get(id=pk)
    user = request.user
    if (Whishlist.objects.filter(old_id=pk).exists()) == False:
        new_item = Whishlist.objects.create(image=image, description=description, price=price, user=user, old_id=pk)
    return redirect('sofas')

def Beds(request, pk):
    image = Additem.objects.values_list('image', flat=True).get(id=pk)
    description = Additem.objects.values_list('description', flat=True).get(id=pk)
    price = Additem.objects.values_list('price', flat=True).get(id=pk)
    user = request.user
    if (Whishlist.objects.filter(old_id=pk).exists()) == False:
        new_item = Whishlist.objects.create(image=image, description=description, price=price, user=user, old_id=pk)
    return redirect('beds')


def Chaiselongues(request, pk):
    image = Additem.objects.values_list('image', flat=True).get(id=pk)
    description = Additem.objects.values_list('description', flat=True).get(id=pk)
    price = Additem.objects.values_list('price', flat=True).get(id=pk)
    user = request.user
    if (Whishlist.objects.filter(old_id=pk).exists()) == False:
        new_item = Whishlist.objects.create(image=image, description=description, price=price, user=user, old_id=pk)
    return redirect('chaiselongues')


def Wardrobes(request, pk):
    image = Additem.objects.values_list('image', flat=True).get(id=pk)
    description = Additem.objects.values_list('description', flat=True).get(id=pk)
    price = Additem.objects.values_list('price', flat=True).get(id=pk)
    user = request.user
    if (Whishlist.objects.filter(old_id=pk).exists()) == False:
        new_item = Whishlist.objects.create(image=image, description=description, price=price, user=user, old_id=pk)
    return redirect('wardrobes')


def Shelving_units(request, pk):
    image = Additem.objects.values_list('image', flat=True).get(id=pk)
    description = Additem.objects.values_list('description', flat=True).get(id=pk)
    price = Additem.objects.values_list('price', flat=True).get(id=pk)
    user = request.user
    if (Whishlist.objects.filter(old_id=pk).exists()) == False:
        new_item = Whishlist.objects.create(image=image, description=description, price=price, user=user, old_id=pk)
    return redirect('shelving_units')


def Tables(request, pk):
    image = Additem.objects.values_list('image', flat=True).get(id=pk)
    description = Additem.objects.values_list('description', flat=True).get(id=pk)
    price = Additem.objects.values_list('price', flat=True).get(id=pk)
    user = request.user
    if (Whishlist.objects.filter(old_id=pk).exists()) == False:
        new_item = Whishlist.objects.create(image=image, description=description, price=price, user=user, old_id=pk)
    return redirect('tables')

