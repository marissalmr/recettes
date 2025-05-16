from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required #Peut pas y accèder si t'es pas connecter 
def home_page(request):
     return render(request, 'homepage.html',)


