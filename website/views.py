from django.shortcuts import render,redirect
from django .contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def handlelogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass1')
        myuser = authenticate(username = username, password = pass1)
        if myuser is not None:
            login(request, myuser)
            messages.success(request, 'login success')
            return redirect('/')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('/login')
    return render (request, 'login.html')

def admin(request):
    return render (request, 'admin.html')

def handlesignup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('pass1')
        confirmpassword = request.POST.get('pass2')
        #print(username, email, password, confirmpassword)
        if password != confirmpassword:
            messages.warning(request, 'Password is incorrect')
            return redirect('/signup')
        
        try:
            if User.objects.get(username = username):
                messages.info(request, 'Username is taken')
                return redirect('/signup')
        except:
            pass
        
        try:
            if User.objects.get(email = email):
                messages.info(request, 'Email is taken')
                return redirect('/signup')
        except:
            pass
        myuser = User.objects.create_user(username, email, password)
        myuser.save()
        messages.success(request, 'Signup Successful Please login')
        return redirect('/login')
        
        
    return render(request, 'signup.html')

def handlelogout(request):
    logout(request)
    messages.info(request, 'Login Success')
    return redirect('/login')
    
