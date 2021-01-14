import numpy
from django.shortcuts import render, redirect
from dashboard.models import Additem
from .models import Whishlist, Reviews, Rating, Seller_rating, Product_rating
from django.utils.datastructures import MultiValueDictKeyError
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
    reviews = Reviews.objects.filter(category='chairs')
    product_rating()
    ratings = Product_rating.objects.filter(category='chairs')
    return render(request, 'chairs.html', {'chairs': chairs, 'reviews': reviews, 'ratings': ratings})


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
    reviews = Reviews.objects.filter(category='armchairs')
    product_rating()
    ratings = Product_rating.objects.filter(category='armchairs')
    return render(request, 'armchairs.html', {'armchairs': armchairs, 'reviews': reviews, 'ratings': ratings})


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
    reviews = Reviews.objects.filter(category='chaiselongues')
    product_rating()
    ratings = Product_rating.objects.filter(category='chaiselongues')
    return render(request, 'chaiselongues.html', {'chaiselongues': chaiselongues, 'reviews': reviews, 'ratings': ratings})


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
    reviews = Reviews.objects.filter(category='sofas')
    product_rating()
    ratings = Product_rating.objects.filter(category='sofas')
    return render(request, 'sofas.html', {'sofas': sofas, 'reviews': reviews, 'ratings': ratings})


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
    reviews = Reviews.objects.filter(category='wardrobes')
    product_rating()
    ratings = Product_rating.objects.filter(category='wardrobes')
    return render(request, 'wardrobes.html', {'wardrobes': wardrobes, 'reviews': reviews, 'ratings': ratings})


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
    reviews = Reviews.objects.filter(category='beds')
    product_rating()
    ratings = Product_rating.objects.filter(category='beds')
    return render(request, 'beds.html', {'beds': beds, 'reviews': reviews, 'ratings': ratings})


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
    reviews = Reviews.objects.filter(category='shelving units')
    product_rating()
    ratings = Product_rating.objects.filter(category='shelving units')
    return render(request, 'shelving_units.html', {'shelving_units': shelving_units, 'reviews': reviews, 'ratings': ratings})


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
    reviews = Reviews.objects.filter(category='tables')
    product_rating()
    ratings = Product_rating.objects.filter(category='tables')
    return render(request, 'tables.html', {'tables': tables, 'reviews': reviews, 'ratings': ratings})




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

def rating_review_armchairs(request, pk):
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
        return redirect("armchairs")

def rating_review_sofas(request, pk):
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
        return redirect("sofas")

def rating_review_beds(request, pk):
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
        return redirect("beds")

def rating_review_chaiselongues(request, pk):
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
        return redirect("chaiselongues")

def rating_review_wardrobes(request, pk):
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
        return redirect("wardrobes")

def rating_review_shelving_units(request, pk):
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
        return redirect("shelving_units")

def rating_review_tables(request, pk):
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
        return redirect("tables")


#rating

def seller_rating ():
    repeated_user_id = Rating.objects.all().values_list('user_id')
    unique_user_id = []
    for i in repeated_user_id:
        if i not in unique_user_id:
            unique_user_id.append(i)

    unique_user_id = numpy.array(unique_user_id)

    waiting_avg_list = []
    for i in unique_user_id:
        waiting_avg_list.append(Rating.objects.values_list('rating', flat=True).filter(user_id=i))

    avg_list = []
    for i in waiting_avg_list:
        avg_list.append(int((sum(i) / len(i))))

    count = 0
    for i in avg_list:
        id = unique_user_id[count]
        print(id)
        if (Seller_rating.objects.filter(user_id=id).exists()) == False:
            new_ratingrow = Seller_rating.objects.create(user_id=id, rating=i)
        else:
            instance = Seller_rating.objects.get(user_id=id)
            instance.rating = i
            #instance.user_id = id
            instance.save()
            #update_rating = Seller_rating.objects.update(rating=i)
        count=count+1


def product_rating ():
    repeated_id = Rating.objects.all().values_list('item_id')
    unique_id = []
    for i in repeated_id:
        if i not in unique_id:
            unique_id.append(i)

    unique_id = numpy.array(unique_id)

    waiting_avg_list = []
    for i in unique_id:
        waiting_avg_list.append(Rating.objects.values_list('rating', flat=True).filter(item_id=i))
    avg_list = []
    for i in waiting_avg_list:
        avg_list.append(int((sum(i) / len(i))))
    count = 0
    for i in unique_id:
        img = Additem.objects.values_list('image', flat=True).get(id=i)
        category = Additem.objects.values_list('category', flat=True).get(id=i)
        rating = avg_list[count]
        if (Product_rating.objects.filter(item_id=i).exists()) == False:
            new_ratingrow = Product_rating.objects.create(item_id=i, img=img, rating=rating, category=category)
        else:
            instance = Product_rating.objects.get(item_id=i)
            instance.rating = rating
            instance.save()
        count = count +1
