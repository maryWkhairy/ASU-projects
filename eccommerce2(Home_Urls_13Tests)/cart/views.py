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
    paid= Total_for_user.objects.filter(product_id=pk).values_list('amount_paid', flat=True).get(product_id=pk)
    q = Total_for_user.objects.filter(product_id=pk,user=request.user).values_list('quantity', flat=True).get(product_id=pk,user=request.user)
    tt = Total.objects.filter(user=request.user).values_list('total', flat=True).get(user=request.user)
    x=str(items_ordered[0])
    ids=Add_to_cart.objects.filter(product_id=x,user=request.user).values_list('product_id',flat=True)
    if x in ids:
        flag = 1
    if flag == 1:
        print('is included')
    else:
        user = Add_to_cart(username=user_name, user=request.user, product_id=items_ordered, image=image,
                           description=description, price=price, total=paidd,product_quantity=amount, quantity=q, paid_amount=tt)
        user.save()
    return render(request, 'chairs.html')


def show_items(request):
    product = Add_to_cart.objects.filter(user=request.user)
    return render(request, 'cart.html', {'products':product})


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

    price = float(Additem.objects.filter(id=pk).values_list('price',flat=True).get(id=pk))
    print(price)
    paid = price * quantity
    Total_for_user(product_id=pk, user=request.user,quantity_ordered=quantity,amount_paid=paid).save()


    paid = Total_for_user.objects.filter(user=request.user).values_list('amount_paid', flat=True)
    print(paid)
    for item in paid:
        total = total + item
    print(total)
    return render(request,'cart.html',{'products':product})