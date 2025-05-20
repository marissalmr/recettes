from . import forms
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required




@login_required #Peut pas y accèder si t'es pas connecter 
def home_page(request):
     return render(request, 'homepage.html',)


def create_recipes(request):
     form = forms.Creation()
     if request.method == "POST":
          form = forms.Creation(request.POST)
          if form.is_valid():
              recipe = form.save(commit=False)
              recipe.user = request.user
              recipe.save()
              return redirect('home_page')
          else :
               form = forms.Creation()
     return render(request, 'recipes_creation.html', {'form': form})
              


              




