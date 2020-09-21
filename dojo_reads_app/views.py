from django.shortcuts import render, redirect
from .models import User, UserManager
from django.contrib import messages
import bcrypt

def index(request):
    return render(request, 'index.html')

def show_books(request):
    return render(request, 'books.html')

def add_book(request):
    return render(request, 'add_book.html')

def show_book(request, id):
    return render(request, 'show_book.html')

def show_user(request, id):
    return render(request, 'show_user.html') 
    
def login(request):
    errors = User.objects.login_validator(request.POST)
    
    if len(errors) > 0:
        # grab each error and have them ready for the view to display 
        for key, value in errors.items():
            messages.error(request, value)
        # return to the page that you were on, the login page and have the user try again
        return redirect('/')
    else:
    # see if the username provided exists in the database
        user = User.objects.filter(email=request.POST['email']) 
        if user: # note that we take advantage of truthiness here: an empty list will return false
            logged_user = user[0] 
            # assuming we only have one user with this username, the user would be first in the list we get back
            # of course, we should have some logic to prevent duplicates of usernames when we create users
            # use bcrypt's check_password_hash method, passing the hash from our database and the password from the form
            if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
                # if we get True after checking the password, we may put the user id in session
                request.session['logged_in_user'] = logged_user.id
                # never render on a post, always redirect!copy
                return redirect('/home')
        # if we didn't find anything in the database by searching by username or if the passwords don't match, 
        # redirect back to a safe route
        return redirect("/")
    
def register(request):
    errors = User.objects.register_validator(request.POST)
    
    if len(errors) > 0:
        # grab each error and have them ready for the view to display 
        for key, value in errors.items():
            messages.error(request, value)
        # return to the page that you were on, the login page and have the user try again
        return redirect('/')
    else:
        # register the user, store them in the database and do whatever else is needed for this project
        hashedPassword = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt(rounds = 14)).decode()
        
        formData = request.POST

        new_user = User.objects.create(
            first_name = formData['first_name'],
            last_name = formData['last_name'],
            email = formData['email'],
            password = hashedPassword
        )
        
        request.session['logged_in_user'] = new_user.id
        return redirect("/home")
    
def add_book_and_review(request):
    pass

def add_review_to_book(request, id):
    pass
    
def logout(request):
    del request.session['logged_in_user']
    return redirect("/")
    