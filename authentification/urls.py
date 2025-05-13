from django.urls import path

import authentification.views

urlpatterns = [
    path('signup/', authentification.views.signup_page, name='signup'),
    path('signon/', authentification.views.login_page, name='signon'),

]