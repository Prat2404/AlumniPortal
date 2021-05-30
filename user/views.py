from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth,AnonymousUser
from django.contrib import messages
# Create your views here.

def signup(request):
    if not request.user.is_anonymous:
        return redirect('/feed/')
    if request.method=='POST':
        first_name = request.POST['name']
        last_name = request.POST['lname']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['pass']
        password2 = request.POST['re_pass']
        if first_name=="" or username=="" or email=="" or password1=="":
           messages.error(request,'Empty fields not allowed')
           return render(request,'user/signup.html')
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.error(request,'username already exist')
            elif User.objects.filter(email=email).exists():
                messages.error(request,'email already exist')
            else:
                user = User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password1)
                user.save()
                return redirect('/user/login')
        else:
            messages.error(request,'password not matching')
    return render(request,'user/signup.html')

def login(request):
    if not request.user.is_anonymous:
        return redirect('/feed/')
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['pass']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/feed')
        else:
            messages.error(request,'Invalid username or password')
    
    return render(request,'user/login.html')

def logout(request):
    auth.logout(request)
    return redirect('/user/login')
