from django.shortcuts import render, HttpResponseRedirect
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from django.contrib import auth
from django.urls import reverse

def login(request):
    if request.method == 'POST':
        context = {
            'form': UserLoginForm(data=request.POST)
        }
        if context['form'].is_valid():
            user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
    else:
        context = {
            'form': UserLoginForm()
        }

    context['title'] = 'Store - Авторизация'
    return render(request, 'users/login.html', context)


def registration(request):

    if request.method == 'POST':
        context = {
            'form': UserRegistrationForm(data=request.POST)
        }
        if context['form'].is_valid():
            context['form'].save()
            return HttpResponseRedirect(reverse('users:login'))
    else:
        context = {
            'form': UserRegistrationForm()
        }
    context['title'] = 'Store - Регистрация'
    return render(request, 'users/registration.html', context)


def profile(request):
    if request.method == 'POST':
        context = {
            'form': UserProfileForm(instance=request.user, data=request.POST, files=request.FILES)
        }
        if context['form'].is_valid():
            context['form'].save()
            return HttpResponseRedirect(reverse('users:profile'))
    else:
        context = {
            'form': UserProfileForm(instance=request.user)
        }
    context['title'] = 'Store - Профиль'
    
    return render(request, 'users/profile.html', context)