from django.conf import settings
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect, render

from . import forms


def signup_page(request):
    form = forms.SignupForm()
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            # auto-login user
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request, 'signup.html', context={'form': form})


def login_page(request):
    form = forms.LoginForm()
    message = ''
    user = None
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
    if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
    if user is not None:
                login(request, user)
                message = f'Bonjour, {user.username}! Vous êtes connecté.'
    else:
                message = 'Identifiants invalides.'
    return render(request, 'signon.html', context={'form': form, 'message': message})
    