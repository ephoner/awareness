from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
# from seo.models import Site
from accounts.forms import UserLoginFrom, UserCreationForm
# Create your views here.

def login_view(request):
    form = UserLoginFrom(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('dashboard')
    return render(request, 'user/login.html', locals())

def register_view(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get("password")
        user.save()
        authenticate(username=user.username, password=password)
        login(request, user=user)
        redirect('/')
    return render(request, 'user/register.html', locals())


def dashboard_view(request):



    return render(request, 'user/dashboard.html', locals())


def user_profile(request):

    return render(request, 'user/user_profile.html', locals())


def my_site(request):
    return render(request, 'user/my_site.html', locals())


def find_links(request):

    return render(request, 'user/find_links.html', locals())

def logout_view(request):
    logout(request)
    return redirect('/')