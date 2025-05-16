from django.urls import path

import accueil.views


urlpatterns = [
    path('homepage/', accueil.views.home_page, name='home_page')
    

]