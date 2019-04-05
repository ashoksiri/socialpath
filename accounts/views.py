from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


# Create your views here.
@login_required
def home(request):
    return render(request,template_name='accounts/index.html',context={})


def login(request):
    if not request.user.is_anonymous:
        print(request.user)
        return redirect('accounts:index')
    return render(request,template_name='accounts/login.html',context={})

def register(request):
    return render(request,template_name='accounts/register.html',context={})


def acc_logout(request):
    """
    Logs out the user and displays 'You are logged out' message.
    """
    logout(request)
    return redirect('accounts:login')
