from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages

def signup(request):
    if request.method == "POST":
        email = request.POST.get("email")
        pass1 = request.POST.get("password")
        pass2 = request.POST.get("confirm_password")

        if pass1 != pass2:
            messages.warning(request, "Those passwords didn’t match. Try again.")
            return redirect("/auth/signup/")
        try:
            if User.objects.get(username=email):
                messages.warning(request, "That username is taken. Try another.")
                return redirect("/auth/signup/")
        except User.DoesNotExist:
            pass

        my_user = User.objects.create_user(email, email, pass1)
        my_user.save()
        my_user = authenticate(username=email, password=pass1)

        if my_user is not None:
            auth_login(request, my_user)
            messages.success(request, "User is created! Log In successful.")
            return redirect("/about")

    return render(request, 'signup.html')

def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        pass1 = request.POST.get("password")

        myuser = authenticate(username=email, password=pass1)

        if myuser is not None:
            auth_login(request, myuser)
            messages.success(request, "Log In successful!")
            return redirect("/about")
        else:
            messages.error(request, "Invalid Credentials!")
            return redirect("/auth/login/")
    
    return render(request, 'login.html')

def logout_view(request):
    auth_logout(request)
    messages.success(request,"Log Out Success!")
    return redirect('/auth/login/')
