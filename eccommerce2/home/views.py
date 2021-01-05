from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def reg(request):
    return render(request, 'reg.html')

def log(request):
    return render(request,'log.html')