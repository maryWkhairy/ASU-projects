from django.shortcuts import render
from .models import Image, Additem
from .forms import ImageForm, AdditemForm

# Create your views here.


def home(request):
    return render(request, 'home.html')


def reg(request):
    return render(request, 'reg.html')


def log(request):
    return render(request, 'log.html')


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
