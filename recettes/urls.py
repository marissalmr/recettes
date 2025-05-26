from django.urls import path

from recettes import views


urlpatterns = [
    path('homepage/',views.home_page, name='home_page'),
    path('create_recipes/', views.create_recipes, name = 'create_recipes'),
    path('recipes_details/<id>/', views.recipe_details, name="recipes_details"),
    #path('recipe_details/<id>/recipe_update', views.recipe_update, name='recipe_update'),
    path('my_recipes/', views.my_recipes, name="my_recipes")



]