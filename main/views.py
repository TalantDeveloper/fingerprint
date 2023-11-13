from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/home')

    return render(request, 'main/login.html')


def logout_view(request):
    logout(request)
    return redirect('main:login')


@login_required
def welcome_view(request):

    return render(request, 'main/welcome.html')
