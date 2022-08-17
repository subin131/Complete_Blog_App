from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
# Create your views here.
def  register(request):
    if request.method=="GET":
        return render(request,'register.html')
    else:
        fn=request.POST['firstname']
        ln=request.POST['lastname']
        email=request.POST['email']
        uname=request.POST["username"]
        password=request.POST['password']
        
        User.objects.create_user(first_name=fn,last_name=ln,email=email,username=uname,password=password)
        return redirect ("home")
    
def signup(request):
    if request.method=="GET": 
        return render(request,'login.html')
    else:
        uname=request.POST["username"]
        paswd=request.POST['password']
        
        user=authenticate(username=uname,password=paswd)
        if user is not None:
            login(request,user)
            #dictionary get feature
            next_url=request.GET.get('next')
            if next_url:
                return redirect(next_url)
            #else
            return redirect("home")
        else:
            return redirect("login")
        
def signout(request):
    logout(request)
    return redirect("login")