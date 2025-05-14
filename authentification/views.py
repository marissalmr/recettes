from django.conf import settings
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect, render

from . import forms


def signup_page(request):
    form = forms.SignupForm()
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            user = form.save() #enregistre utilisateur en bdd et stock en variable
            # auto-login user
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request, 'signup.html', context={'form': form})


def login_page(request): #Demande que je fais au serveur en cliquant = requete est un objet
    form = forms.LoginForm() #On appelle la classe login Form 
    message = ''
    user = None
   # print(request.method)
    if request.method == 'POST': #Si je poste des données
        form = forms.LoginForm(request.POST) #on rentre les données dans le formulaire
       # print(request.POST)
    #print(form.is_valid())
    if form.is_valid(): #Si tout les champs on été rentré et qu'il respecte les conditions (max50 caracteres...)
            user = authenticate( #Cette méthode elle va servir à vérifier que la personne existe dèja dans la BDD
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            #print(user) = Si la personne existe dans la BDD on verra son nom, sinon c'est none
            
    if user is not None: #Dans le cas ou on le trouve dans la BDD
                login(request, user)
                message = f'Bonjour, {user.username}! Vous êtes connecté.'
                
    else:
                message = 'Identifiants invalides.'
    return render(request, 'signon.html', context={'form': form, 'message': message}) #Le render permet d'afficher la page html
    