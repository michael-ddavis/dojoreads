from django.urls import path
from . import views 

# index (/)  - Login Registration Page HTML (GET)
# success (/success) - Logged In page HTML (GET)

urlpatterns = [
    path('', views.index),
    path('home', views.home),
    path('logout', views.logout),
    # Invisible routes 
    # login - (/login) Logs the user in (POST)
    # register - (/register) Registers the user (POST)
    
    path('login', views.login),
    path('register', views.register)
]
