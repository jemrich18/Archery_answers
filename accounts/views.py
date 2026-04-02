from django.shortcuts import render, redirect 
from django.contrib.auth import login, authenticate, logout 
from django.contrib import messages 
from .forms import RegisterForm 
from .models import ArcherProfile

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            ArcherProfile.objects.create(user=user)
            login(request, user)
            messages.success(request, 'welcome to Archery Answers!')
            return redirect('calculator:home')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('calculator:home')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'accounts/login.html')


def logout_view(request):
    logout(request)
    return redirect('calculator:home')