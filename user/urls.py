from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views


app_name = 'user'
urlpatterns = [
    # Login
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='login' ),

    #Logout page. 
    path('logout/', views.logout_user, name='logout'),

    # Register a new user.
    path('register/', views.register, name='register')
]
