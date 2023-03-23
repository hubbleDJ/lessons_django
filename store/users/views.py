from django.shortcuts import render
from users.forms import UserLoginForm


def login(request):
    context = {
        'title': 'Store - Авторизация',
        'form': UserLoginForm()
    }
    return render(request, 'users/login.html', context)

def registration(request):
    context = {
        'title': 'Store - Регистрация',
    }
    return render(request, 'users/registration.html', context)