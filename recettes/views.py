from . import forms
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Recettes
from .forms import Comments


@login_required #Peut pas y accèder si t'es pas connecter 
def home_page(request):
     all_recette= Recettes.objects.all()
     context = {
        'recettes' : all_recette,
     }
     return render(request, 'homepage.html', context=context )

@login_required
def create_recipes(request): #demande envoyée par l'user au serveur
     form = forms.Creation() #Formulaire vide
     if request.method == "POST": #L'utilisateur envoie des données
          form = forms.Creation(request.POST)
          if form.is_valid():
              recipe = form.save(commit=False) #Crée l'objet recette en mémoire (avec les données du formulaire) mais ne l'enregistre pas encore en BDD car il manque le champ user
              recipe.user = request.user #« Cette recette a été créée par l’utilisateur actuellement connecté »
              recipe.save() #Et mtn qu'on a tout ce dont on a besoin, on enregistre l'objet complet (avec le user) en BDD
              return redirect('home_page')
          if request.method == "GET":
               form = forms.Creation()
     return render(request, 'recipes_creation.html', {'form': form}) #Que le formulaire soit envoyée ou pas, on affiche la page HTML avec le formulaire

@login_required 
def recipe_details(request, id):
     recette = get_object_or_404(Recettes, id=id)
     commentaires = recette.commentaires_set.all() #donne moi tous les commentaires lié à cette recette
     return render(request, 'recipes_details.html', {'recette': recette, 'commentaires':commentaires}) #dictionnaire = variable a utiliser dans le template

@login_required
def my_recipes(request):
     mes_recettes = Recettes.objects.filter(user=request.user)
     return render(request, 'homepage.html', {'recettes': mes_recettes, 'source': 'my_recipes', "source2": "delete"})

@login_required
def recipe_update(request, id_from_url):
     recette = get_object_or_404(Recettes,id=id_from_url, user=request.user) #id = id de la recette qu'on veut affichert via l'url et elle doit appartenir à l'utilisateur connécté
     if request.method == "GET":
          form = forms.Creation(instance=recette)
          return render(request, 'recipes_creation.html', {'form': form} )
     if request.method == "POST":
          form = forms.Creation(request.POST, instance=recette)
          if form.is_valid():
              recipe = form.save()
          return redirect('home_page')
    
@login_required
def recipe_delete(request, id_from_url): #Identifiant de la recette à supprimer transmis depuis l'url pour pas supprimer les autres qui ne viennent pas de nous
     mes_recette = get_object_or_404(Recettes, id=id_from_url, user=request.user) #On récuppere l'objet recette qui à le bon identifiant et qui a été crée par l'utilisateur connécté
     if request.method == "POST": #Pas de delete car le HTML ne traite que des GET (via <a>) et des POST via <form method="POST"> 
          mes_recette.delete()

          #return render(request, 'homepage.html', {'recettes': rafraichissement_page, 'source2': 'delete_recipes'})

     return redirect('my_recipes')

@login_required
def add_comments(request, recette_id): #identifiant de la recette ciblé
    recette = Recettes.objects.get(id=recette_id) #Rattacher le commentaire a une recette précise via son id 

    if request.method == "POST":
        form = Comments(request.POST)
        if form.is_valid():
            commentaire = form.save(commit=False) #Foreign key pas demandé à l'user donc on met pas tout de suite en BDD pour le mettre juste en bas 
            commentaire.recettes = recette #On associe le commentaire à la recette sélectionnée
            commentaire.user = request.user #On associe le commentaire à l'utilisateur connécté
            commentaire.save()
            return redirect("home_page")
    else:  
        form = Comments()

    return render(request, "recipes_details.html")
          



     
     



              




