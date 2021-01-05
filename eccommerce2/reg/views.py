from django.shortcuts import render,redirect
from django.contrib.auth.models import auth,User
from django.contrib import messages

# Create your views here.

def reg(request):
    if request.method=='POST':
        username = request.POST['username']
        # first_name = request.POST['firstname']
        # last_name = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        password_confirm = request.POST['password1']


        if password == password_confirm:
            if User.objects.filter(username=username).exists():
                messages.info(request, "!! username taken")
                return redirect('/reg')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                print('user created')
                return redirect('/log')
        else:
            messages.info(request, "!! passwords aren't matching")
            return redirect('/reg')
    else:
        return render(request,'reg.html')


def log(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request,user)
            print('success')
            return redirect('/')

        else:
            messages.info(request, "!! incorrect data")
            return redirect('/log')

    else:
        return render(request, 'log.html')

