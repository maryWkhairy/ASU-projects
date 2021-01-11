from django.shortcuts import render, redirect
from .models import Register, Image, Additem
from .forms import ImageForm, AdditemForm


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
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # image_test = form.instance
            images = Image.objects.all()
            return render(request, 'register.html', {'imagess': images})  # {'form': form},
    # imge = request.POST['image']
    # sav = Image.objects.create(
    #   image=imge,
    # )

    # return redirect('home')
    else:
        form = ImageForm()
        images = Image.objects.all()
        return render(request, 'register.html', {'form': form, 'imagess': images})


def cart(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # image_test = form.instance
            images = Image.objects.all()
            return render(request, 'cart.html', {'form': form, 'imagess_html': images})

    else:
        form = ImageForm()
        images = Image.objects.all()
        return render(request, 'cart.html', {'form': form, ' imagess_html': images})


def dashboard(request):
    if request.method == 'POST':
        form = AdditemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
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


def home(request):
    return render(request, 'home.html')
