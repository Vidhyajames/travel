from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

def login(request):
    if request.method =='POST':
        username=request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid Credentials")
            return redirect('login')
    return render(request,"login.html")


def register(request):
    if request.method =='POST':
        username=request.POST['username']
        firstname=request.POST['first_name']
        lastname=request.POST['last_name']
        emailid=request.POST['email']
        password=request.POST['password']
        confirm_password = request.POST['password1']
        if password==confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Existing User")
                return redirect('register')
            elif User.objects.filter(email=emailid).exists():
                messages.info(request,"Existing Email Id")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password,first_name=firstname,last_name=lastname,email=emailid)
                user.save();
                return redirect('login')
                print("user created")
        else:
            messages.info(request,"Mismatch in Password")
            return redirect('register')
        return redirect('/')
    return render(request,"register.html")
def logout(request):
    auth.logout(request)
    return redirect('/')






# Create your views here.
