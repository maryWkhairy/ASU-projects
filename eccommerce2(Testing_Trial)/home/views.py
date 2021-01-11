from django.shortcuts import render
from dashboard.models import Additem


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
    return render(request, 'chairs.html', {'chairs': chairs})


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
