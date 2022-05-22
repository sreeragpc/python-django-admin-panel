from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.

def user_login(request):
    if request.user.is_authenticated:
        return redirect(home)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(home)
        else:
            messages.error(request,'invalid credentials')

    return render(request, 'login.html')

def home(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    return redirect(user_login)    

def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect(user_login)        

def register(request):

    if request.method == 'POST':
        username = request.POST['username']
        password= request.POST['password']


        user = User.objects.create_user(username = username , password = password )
        user.save()
        print('user created')
        return redirect(user_login)

    return render(request,'register.html')    