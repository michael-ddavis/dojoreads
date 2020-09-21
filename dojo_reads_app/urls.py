from django.urls import path
from . import views 

# index (/)  - Login Registration Page HTML (GET)
# success (/success) - Logged In page HTML (GET)

urlpatterns = [
    path('', views.index),
    path('logout', views.logout),
    path('books', views.show_books),
    path('books/add', views.add_book),
    path('books/<int:id>', views.show_book),
    path('books/users/<int:id>', views.show_user),
    
    # Invisible routes 
    # login - (/login) Logs the user in (POST)
    # register - (/register) Registers the user (POST)
    # add book and review  - adds a book and its review to the 
    
    path('login', views.login),
    path('register', views.register),
    path('add_book_and_review', views.add_book_and_review),
    path('add_review/<int:id>', views.add_review_to_book)
]
