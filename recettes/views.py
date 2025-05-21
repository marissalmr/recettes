from . import forms
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required




@login_required #Peut pas y accèder si t'es pas connecter 
def home_page(request):
     return render(request, 'homepage.html',)

@login_required
def create_recipes(request): #demande envoyée par l'user au serveur
     form = forms.Creation() #Formulaire vide
     if request.method == "POST": #L'utilisateur envoie des données
          form = forms.Creation(request.POST)
          if form.is_valid():
              recipe = form.save(commit=False)
              recipe.user = request.user
              recipe.save() 
              return redirect('home_page')
          if request.method == "GET":
               form = forms.Creation()
     return render(request, 'recipes_creation.html', {'form': form}) #Que le formulaire soit envoyée ou pas, on affiche la page HTML avec le formulaire
              


              




