from operator import imod
from tkinter import Button
from urllib.request import Request
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from secondadmin.form import UserdataForm

# Create your views here.




def adminlogin(request):
    if request.user.is_authenticated:
        return redirect(adminhome)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(adminhome)
        else:
            messages.error(request,'invalid credentials')

    return render(request, 'adminlogin.html')

def adminhome(request):
    b=User.objects.all()
    if request.user.is_authenticated:
        return render(request, 'adminhome.html',{'b':b})
    return redirect(adminlogin)    

def adminlogout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect(adminlogin)        

# b = User.objects.create(username='meee', password='1234')

# c=User.objects.get(username='jaliba')
# c.delete()

# a=User.objects.get(username='shahid')
# a.username='shahid1'
# a.save()

def admindelete(request,value):
    if User.objects.filter(id=value).count() > 0:
        c=User.objects.get(id=value)
        c.delete() 
    return redirect('adminhome') 


def adminadd(request):
    submit="<button><input type=\"submit\"><button>"
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        User.objects.create_user(username=username,password=password)
        return adminhome(request)
    p=User.objects.all()
    context={
        'b':p,
        'h':submit,
        'form':UserdataForm()
    }
    
    return render(request,'adminhome.html',context)    

def adminupdate(request,id):
    user=User.objects.get(id=id)
    context = {
        'user':user
    }
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user.username=username
        user.set_password(password)
        user.save()
        return redirect(adminhome)
    return render(request, 'adminupdate.html', context)