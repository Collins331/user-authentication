from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required 
from django.contrib import messages



# Create your views here.

def home(request):
    return render(request, 'index.html')


def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully")
            return redirect('login')
        messages.warning(request, "Your details are invalid")
        
    return render(request, 'register.html', {'form': form})



def user_login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, f"You have logged in successfully as {username}")
                return redirect('home')
        messages.warning(request, "Your details are invalid")
            
    
    return render(request, 'login.html', {'form': form})


def user_logout(request):
    logout(request)
    messages.success(request, "You have logged out successfully")
    return redirect('home')
        
