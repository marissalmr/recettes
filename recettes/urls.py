from django.urls import path

from recettes import views


urlpatterns = [
    path('homepage/',views.home_page, name='home_page'),
    path('create_recipes/', views.create_recipes, name = 'create_recipes'),
    path('all-recipes/', views.home_page, name='all_recettes')



]