from . import forms
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Recettes


@login_required #Peut pas y accèder si t'es pas connecter 
def home_page(request):
     all_recette= Recettes.objects.all()
     print(all_recette)
     context = {
        'recettes' : all_recette 
     }
     return render(request, 'homepage.html', context=context )

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

@login_required
def recipe_details(request, id):
     recette = get_object_or_404(Recettes, id=id)
     return render(request, 'recipes_details.html', {'recette': recette})

def my_recipes(request):
     print(request.user)
     mes_recettes = Recettes.objects.filter(user=request.user)
     return render(request, 'my_recipes.html', {'mes_recettes': mes_recettes})

#def recipe_update(request, id):
     #recette = Recettes.objects.get(id=id)
     #form = forms.Creation(instance=Recettes)
     #return render (request,)



              




