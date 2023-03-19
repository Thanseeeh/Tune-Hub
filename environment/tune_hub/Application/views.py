from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
import re

# Create your views here.


def signup(request):
    if 'username' in request.session:
        return redirect(index)
    if request.method == 'POST':
        first_name = request.POST['first_name']
        username = request.POST['username']
        email =request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        # space validation 
        if first_name.strip() == "" or username.strip() == "" or email.strip() == "" or password.strip() == "" or confirm_password.strip() == "":
            messages.info(request, 'Enter the required Fields')
            return redirect(signup)
        
        # first_name validation
        if not re.match(r'^[a-zA-Z]{3,20}$', first_name):
            messages.info(request, 'First name must be between 3 and 20 characters and contain only alphabets')
            return redirect(signup)
        
        # Username validation
        if not re.match(r'^.{3,20}$', username):
            messages.info(request, 'Username must be between 3 and 20 characters')
            return redirect(signup)
        
        # Email validation
        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
            messages.info(request, 'Invalid email format')
            return redirect(signup)
        
        # Password validation
        if not re.match(r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{5,20}$', password):
            messages.info(request, 'Password must contain at least one letter and one digit, and be between 5 and 20 characters')
            return redirect(signup)
        
        if password==confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username is already taken')
                return redirect(signup) 
            
            if  User.objects.filter(email=email).exists():
                messages.info(request, 'Email is already taken')
                return redirect(signup) 
            
            else:
                user = User.objects.create_user(first_name=first_name, username=username, email=email, password=password)
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


def admin(request):
    data = User.objects.all()
    total_user = data.count()

    context = {'data': data, 'total_user': total_user }
    if 'username' in request.session:
        return render(request, 'admin.html', context)
    else:
        return render(request, 'admin_login.html')

def login_admin(request):
    if 'username' in request.session:
        return redirect(admin)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if username == 'thanseeeeeh' and password == 'ellikkal7':
            # valid credentials, log in the user and redirect to admin page
            request.session['username'] = username
            return redirect('admin')
        else:
            messages.info(request, 'Invalid Username or Password')
            return redirect('login_admin')
    else:
        return render(request, 'admin_login.html')
    

def delete_user(request, user_id):
    user = User.objects.get(id=user_id)
    user.delete()
    return redirect('admin')


def update_user(request, user_id):
    user = User.objects.get(id=user_id)
    user.delete()

    if request.method == 'POST':
        first_name = request.POST['first_name']
        email = request.POST['email']

        # validate the input fields
        if first_name.strip() == "" or email.strip() == "":
            messages.info(request, 'Enter the required Fields')
            return redirect('update_user', user_id=user_id)

        if not re.match(r'^[a-zA-Z]{3,20}$', first_name):
            messages.info(request, 'First name must be between 3 and 20 characters and contain only alphabets')
            return redirect('update_user', user_id=user_id)

        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
            messages.info(request, 'Invalid email format')
            return redirect('update_user', user_id=user_id)

        # update the user
        user.first_name = first_name
        user.email = email
        user.save()

        messages.success(request, 'User updated successfully')
        return redirect('admin')

    context = {'user': user}
    return render(request, 'update_user.html', context)

    


def index(request):
    if 'username' in request.session:
        return render(request, 'index.html')
    else:
        return render(request, 'login.html')


