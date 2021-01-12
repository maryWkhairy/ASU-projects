from django.shortcuts import render
from django.http import HttpResponse
from dashboard.models import Additem
from .models import Add_to_cart,Total_for_user,Total
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
    return render(request, 'chairs.html')


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
        Total(user=request.user,total=total).save()
    Add_to_cart.objects.filter(user=request.user,product_id=pk).update(total=paid_cal,quantity=quantity)
    return render(request,'cart.html',{'products':product,
                                       'total':total})


