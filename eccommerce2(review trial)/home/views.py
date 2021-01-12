import numpy
from django.contrib import messages
import numpy as np
from django.shortcuts import render, redirect
from django.utils.datastructures import MultiValueDictKeyError

from dashboard.models import Additem
from .models import Whishlist, Reviews, Rating


# Create your views here.
def home(request):
    return render(request, 'home.html')


def reg(request):
    return render(request, 'reg.html')


def log(request):
    return render(request, 'log.html')


# Categories
def chairs(request):
    chairs = Additem.objects.filter(category='chairs')
    reviews = Reviews.objects.filter(category='chairs')
    repeated_id = Rating.objects.all().values_list('item_id').filter(category='chairs')

    unique_id =[]
    for i in repeated_id:
        if i not in unique_id:
            unique_id.append(i)

    unique_id = numpy.array(unique_id)

    waiting_avg_list=[]
    for i in unique_id:
        waiting_avg_list.append(Rating.objects.values_list('rating', flat=True).filter(item_id=i))

    avg_list=[]
    for i in waiting_avg_list:
        avg_list.append(int((sum(i) / len(i))/5*100))

    img_list =[]
    for i in unique_id:
        img_list.append(Additem.objects.values_list('image', flat=True).filter(id=i))
    img_list = numpy.array(img_list)

    print(img_list)
    print(avg_list)
    print(waiting_avg_list)
    return render(request, 'chairs.html', {'chairs': chairs, 'reviews': reviews, 'avg_list' : avg_list })


def armchairs(request):
    armchairs = Additem.objects.filter(category='armchairs')
    return render(request, 'armchairs.html', {'armchairs': armchairs})


def chaiselongues(request):
    chaiselongues = Additem.objects.filter(category='chaiselongues')
    return render(request, 'chaiselongues.html', {'chaiselongues': chaiselongues})


def sofas(request):
    sofas = Additem.objects.filter(category='sofas')
    return render(request, 'sofas.html', {'sofas': sofas})


def wardrobes(request):
    wardrobes = Additem.objects.filter(category='wardrobes')
    return render(request, 'wardrobes.html', {'wardrobes': wardrobes})


def beds(request):
    beds = Additem.objects.filter(category='beds')
    return render(request, 'beds.html', {'beds': beds})


def shelving_units(request):
    shelving_units = Additem.objects.filter(category='shelving units')
    return render(request, 'shelving_units.html', {'shelving_units': shelving_units})


def tables(request):
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


def whishlist(request):
    wish_items = Whishlist.objects.filter(user=request.user)
    return render(request, 'whishlist.html', {'wish_items': wish_items})

def remove_from_wish(request, pk):
    Whishlist.objects.filter(id=pk).delete()
    return redirect('whishlist')




#reviews

def rating_review_chairs(request, pk):
    if request.method == 'POST':
        review = request.POST['review']
        img = Additem.objects.values_list('image', flat=True).get(id=pk)
        category = Additem.objects.values_list('category', flat=True).get(id=pk)
        new_review = Reviews.objects.create(review=review, item_id=pk, img=img, category=category)
        try:
            rating = request.POST['rate']
        except MultiValueDictKeyError:
            quantity = 0
        user_id = Additem.objects.values_list('user', flat=True).get(id=pk)
        new_rating = Rating.objects.create(item_id=pk, rating=rating, user_id=user_id, img=img, category=category)
        return redirect("chairs")

#rating

#def product_rating_chairs(request, pk):
 #   if request.method == 'POST':
  #      try:
   #         rating = request.POST['rate']
    #    except MultiValueDictKeyError:
      #      quantity = 0

     #   #print(rating)
       # img = Additem.objects.values_list('image', flat=True).get(id=pk)
        #user_id = Additem.objects.values_list('user', flat=True).get(id=pk)
        #category = Additem.objects.values_list('category', flat=True).get(id=pk)
        #new_rating = Rating.objects.create(item_id=pk, rating=rating, user_id=user_id, img=img, category=category)
        #return redirect('chairs')

