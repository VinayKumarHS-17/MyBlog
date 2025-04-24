from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views

def home(request):
    return render(request,'home.html')


def signup_user(request):
    if request.user.username:
        return redirect("home")
    
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
 
        if password1 == password2:
            if User.objects.filter(username=username):
                messages.error(request,"Username already taken!")
            else:
                user = User.objects.create_user(username=username, email=email, password=password1)
                user.save()
                messages.success(request,"Account created successfully!")
                return redirect("login") 
        else:
            messages.error(request,"Passwords do not match!")
    return render(request, "signup.html",)



def login_user(request):
    if request.user.username:
        return redirect("home")
    
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("pw1")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request,"Login successful!")
            return redirect("home") 
        else:
            messages.error(request,"Invalid credentials!")

    return render(request, "login.html")



def logout_user(request):
    logout(request)
    messages.error(request,"Logged out successfully!")
    return redirect("signup")