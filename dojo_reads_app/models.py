from django.db import models
import re
import bcrypt

class UserManager(models.Manager):
    def register_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(postData['first_name']) < 2:
            errors['first_name'] = "Your First Name should be more than 2 characters!"
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Your Last Name should be more than 2 characters!"
        if not EMAIL_REGEX.match(postData['email']):          
            errors['email'] = "Invalid email address!"
        if len(postData['password']) < 8:
            errors['password'] = "Password should be at least 8 characters"
        if postData['password'] != postData['confirm_password']:
            errors['password'] = "Password and Password confirm must match!"
        return errors
    
    def login_validator(self, postData):
        errors = {}
        user = User.objects.filter(email=postData['email'])
        if user:
            log_user = user[0]
            if not bcrypt.checkpw(postData['password'].encode(), log_user.password.encode()):
                errors['password'] = "Invalid login attempt"
        else:
            errors['password'] = "Invalid login attempt"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length = 45)
    last_name = models.CharField(max_length = 45)
    email = models.CharField(max_length = 255)
    password = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
    
