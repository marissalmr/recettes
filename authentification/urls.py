from django.urls import path
from .views import logout

import authentification.views

urlpatterns = [
    path('signup/', authentification.views.signup_page, name='signup'),
    path('signon/', authentification.views.login_page, name='signon'),
    path('logout/', authentification.views.log_out, name='logout'),
    
    
    

]