#Création du fichier forms.py qui contiendra les formulaires (= convention)
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms #Permet de créer des formulaire HTML en python

#Inscription
class SignupForm(UserCreationForm): #On pars d'un formulaire d'inscription de django qui fournit deja des champs
    class Meta(UserCreationForm.Meta): #Meta est une classe à l"intérieur d'"une classe, pas besoin d'en créer une autre car elle est deja dans le modele de django
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name', 'age', 'niveau_choix') #Je veux que mes formulaires affiche ces champs-la

#Connexion, formulaire html en python = boite vide avec des champs
class LoginForm(forms.Form): 
    username = forms.CharField(max_length=50, label = "Username") #varchar, max 50, sur le site ce sera appelé Username
    password = forms.CharField(max_length=50, widget=forms.PasswordInput, label = "Password") #Widget détermine la façon dont on affiche le champ
