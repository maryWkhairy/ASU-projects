from django.shortcuts import render, redirect
from django.contrib import messages
from dashboard.models import Additem
from .models import Add_to_cart,Total_for_user,Total,checkout_details,User_participation
from django.utils.datastructures import MultiValueDictKeyError
# Create your views here.


def add_to_cart(request,pk):
    #get user logged in
    flag=0
    total=0
    user_name = request.user.username
    #user_added = add to cart.objects.filter(username=user_name)

    # add items to add to cart
    items_ordered = Additem.objects.filter(id=pk).values_list('pk',flat=True)
    image = Additem.objects.filter(id=pk).values_list('image',flat=True).get(id=pk)
    description = Additem.objects.filter(id=pk).values_list('description', flat=True).get(id=pk)
    price = Additem.objects.filter(id=pk).values_list('price', flat=True).get(id=pk)
    amount = Additem.objects.filter(id=pk).values_list('amount', flat=True).get(id=pk)

    x=str(items_ordered[0])
    ids=Add_to_cart.objects.filter(product_id=x,user=request.user).values_list('product_id',flat=True)
    if x in ids:
        flag=1
    if flag==1:
        print('is included')
    else:
        user = Add_to_cart(username=user_name, user=request.user, product_id=items_ordered, image=image,
                           description=description, price=price, product_quantity=amount)
        user.save()


    category = Additem.objects.filter(id=pk).values_list('category',flat=True).get(id=pk)
    print(category)
    if category == 'chairs':
        chairs = Additem.objects.filter(category='chairs')
        return render(request, 'chairs.html', {'chairs': chairs})

    elif category == 'armchairs':
        armchairs = Additem.objects.filter(category='armchairs')
        return render(request, 'armchairs.html', {'armchairs': armchairs})

    elif category == 'chaiselongues':
        chaiselongues = Additem.objects.filter(category='chaiselongues')
        return render(request, 'chaiselongues.html', {'chaiselongues': chaiselongues})

    elif category == 'sofas':
        sofas = Additem.objects.filter(category='sofas')
        return render(request, 'sofas.html', {'sofas': sofas})

    elif category == 'wardrobes':
        wardrobes = Additem.objects.filter(category='wardrobes')
        return render(request, 'wardrobes.html', {'wardrobes': wardrobes})

    elif category == 'beds':
        beds = Additem.objects.filter(category='beds')
        return render(request, 'beds.html', {'beds': beds})

    elif category == 'shelving units':
        shelving_units = Additem.objects.filter(category='shelving units')
        return render(request, 'shelving_units.html', {'shelving_units': shelving_units})

    elif category == 'tables':
        tables = Additem.objects.filter(category='tables')
        return render(request, 'tables.html', {'tables': tables})


def show_items(request):
    product = Add_to_cart.objects.filter(user=request.user)
    return render(request,'cart.html',{'products':product})


def add_quantity(request,pk):
    total=0
    product = Add_to_cart.objects.filter(user=request.user)
    Total_for_user.objects.filter(product_id=pk,user=request.user).delete()

    try:
        quantity = float(request.POST['quantity'])
    except MultiValueDictKeyError:
        quantity = float(1)

    print(quantity)
    print(pk)


    price = Additem.objects.filter(id=pk).values_list('price',flat=True).get(id=pk)
    print(price)
    paid_cal = price * quantity

    Total_for_user(product_id=pk, user=request.user,quantity_ordered=quantity,amount_paid=paid_cal).save()


    paid = Total_for_user.objects.filter(user=request.user).values_list('amount_paid', flat=True)
    print(paid_cal)
    for item in paid:
        total = total + item
    print(total)
    ids = Total.objects.filter(user=request.user).values_list('user',flat=True)
    if ids:
        Total.objects.filter(user=request.user).update(total=total)
    else:
        Total(user=request.user, total=total).save()
    Add_to_cart.objects.filter(user=request.user,product_id=pk).update(total=paid_cal,quantity=quantity)
    final = total + 150 + 100

    return render(request,'cart.html',{'products':product,'total':total,'finals':final})

def remove_cart(request,pk):
    one_item_total = float(Add_to_cart.objects.filter(product_id=pk, user=request.user).values_list('total',flat=True).get(product_id=pk, user=request.user))
    Add_to_cart.objects.filter(product_id=pk, user=request.user).delete()

    product = Add_to_cart.objects.filter(user=request.user)
    total1 = float(Total.objects.filter(user=request.user).values_list('total',flat=True).get(user=request.user))
    total = total1 - one_item_total
    final = total + 150 + 100

    return render(request, 'cart.html',{'products':product,'total':total,'finals':final})

def checkout(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        city = request.POST['city']
        paymentMethod = request.POST['paymentMethod']



        try:
            country = request.POST['country']
        except MultiValueDictKeyError:
            country = 'Egypt'
        try:
            currency = request.POST['currency']
        except MultiValueDictKeyError:
            currency = 'EGP'

        #h = Add_to_cart.objects.filter(user=request.user).values_list('product_id').get(user=request.user)
        h = Add_to_cart.objects.filter(user=request.user).exists()
        if not h:
            messages.info(request, "!! empty cart")
            return redirect('/cart_items')


        else:
            checkout_details(username=username,email=email, phone=phone,address=address,city=city,country=country,
                             currency=currency,paymentMethod=paymentMethod).save()

            #particpation
            get_count = User_participation.objects.filter(user=request.user).values_list('count',flat=True).get(user=request.user)
            print(get_count)
            if get_count:
                inc_count = int(get_count) +1
                User_participation.objects.filter(user=request.user).update(count=inc_count)
            else:
                User_participation(user=request.user,count=1).save()

            Add_to_cart.objects.filter(user=request.user).delete()
            print('order completed')
            return redirect('/confirm')
    else:
        return render(request, 'checkout.html')


def offers(request):
    return render(request,'offers.html')

def confirm(request):
    return render(request,'confirm.html')