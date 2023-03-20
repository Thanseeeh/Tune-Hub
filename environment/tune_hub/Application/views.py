from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from .models import Musics
import re
from django.db.models import Q

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
    content = Musics.objects.all()
    total_user = data.count()
    total_music = content.count()

    query = request.GET.get('q')
    if query:
        data = data.filter(
            Q(first_name__icontains=query)
        )


    if request.method == 'POST':
        first_name = request.POST['first_name']
        username = request.POST['username']
        email =request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        # space validation 
        if first_name.strip() == "" or username.strip() == "" or email.strip() == "" or password.strip() == "" or confirm_password.strip() == "":
            messages.info(request, 'Enter the required Fields')
            return redirect(admin)
        
        # first_name validation
        if not re.match(r'^[a-zA-Z]{3,20}$', first_name):
            messages.info(request, 'First name must be between 3 and 20 characters and contain only alphabets')
            return redirect(admin)
        
        # Username validation
        if not re.match(r'^.{3,20}$', username):
            messages.info(request, 'Username must be between 3 and 20 characters')
            return redirect(admin)
        
        # Email validation
        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
            messages.info(request, 'Invalid email format')
            return redirect(admin)
        
        # Password validation
        if not re.match(r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{5,20}$', password):
            messages.info(request, 'Password must contain at least one letter and one digit, and be between 5 and 20 characters')
            return redirect(admin)
        
        if password==confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username is already taken')
                return redirect(admin) 
            
            if  User.objects.filter(email=email).exists():
                messages.info(request, 'Email is already taken')
                return redirect(admin) 
            
            else:
                user = User.objects.create_user(first_name=first_name, username=username, email=email, password=password)
                user.set_password(password) 
                user.save()
                return redirect(admin)
        
        else:
            messages.info(request, 'Both passwords are not matching')
            return redirect(admin)
    
    context = {'data': data, 'total_user': total_user, 'content': content, 'total_music': total_music }
    if 'thanseeeeeh' in request.session:
        return render(request, 'admin.html', context)
    
    else:
        return render(request, 'admin_login.html')
    

def login_admin(request):
    if 'thanseeeeeh' in request.session:
        return redirect(admin)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if username == 'thanseeeeeh' and password == 'ellikkal7':
            # valid credentials, log in the user and redirect to admin page
            request.session['thanseeeeeh'] = username
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
        username = request.POST['username']
        email =request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        # space validation 
        if first_name.strip() == "" or username.strip() == "" or email.strip() == "" or password.strip() == "" or confirm_password.strip() == "":
            messages.info(request, 'Enter the required Fields')
            return redirect(update_user)
        
        # first_name validation
        if not re.match(r'^[a-zA-Z]{3,20}$', first_name):
            messages.info(request, 'First name must be between 3 and 20 characters and contain only alphabets')
            return redirect(update_user)
        
        # Username validation
        if not re.match(r'^.{3,20}$', username):
            messages.info(request, 'Username must be between 3 and 20 characters')
            return redirect(update_user)
        
        # Email validation
        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
            messages.info(request, 'Invalid email format')
            return redirect(update_user)
        
        # Password validation
        if not re.match(r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{5,20}$', password):
            messages.info(request, 'Password must contain at least one letter and one digit, and be between 5 and 20 characters')
            return redirect(update_user)
        
        if password==confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username is already taken')
                return redirect(update_user) 
            
            if  User.objects.filter(email=email).exists():
                messages.info(request, 'Email is already taken')
                return redirect(update_user) 
            
            else:
                user = User.objects.create_user(first_name=first_name, username=username, email=email, password=password)
                user.set_password(password) 
                user.save()
                return redirect('admin')
        
        else:
            messages.info(request, 'Both passwords are not matching')
            return redirect(update_user)
    else:
        context = {'user': user}
        return render(request, 'update_user.html', context)

    


def index(request):
    if 'username' in request.session:
        music_data = Musics.objects.all()
        context = {'music_data': music_data}
        return render(request, 'index.html', context)
    else:
        return render(request, 'login.html')


