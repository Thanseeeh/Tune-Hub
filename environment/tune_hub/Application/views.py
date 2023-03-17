from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth

# Create your views here.


def signup(request):
    if 'username' in request.session:
        return redirect(index)
    if request.method == 'POST':
        username = request.POST['username']
        phone = request.POST['phone']
        email =request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if username.strip() == "" or phone.strip() == "" or email.strip() == "" or password.strip() == "" or confirm_password.strip() == "":
            messages.info(request, 'Enter the required section')
            return redirect(signup)
        if password==confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Email is exist')
                return redirect(signup) 
            else:
                user = User.objects.create_user(username=username, phone=phone, email=email, password=password)
                user.set_password(password) 
                user.save()
                return redirect('login_user')
        
        else:
            messages.info(request, 'Both passwords are not matching')
            return redirect(signup)
    else:
        return render(request, 'signup.html')
    

def login_user(request):
    if 'username' in request.session:
        return redirect(index)
    if request.method == 'POST':
        username =request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            request.session['username'] = username
            auth.login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Invalid Username or Password')
            return redirect('login_user')
    else:
        return render(request, 'login.html')
    

def logout_user(request):
    auth.logout(request)
    return redirect('login_user')


def index(request):
    return render(request, 'index.html')

def admins(request):
    return render(request, 'admin.html')
