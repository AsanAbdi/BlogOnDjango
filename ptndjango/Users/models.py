from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser, BaseUserManager

from django.shortcuts import reverse



class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        if email is None:
            raise TypeError('Users must have an email address.')

        user = self.model(email=self.normalize_email(email), **kwargs)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password):
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user



# Create your models here.
class User(AbstractUser):
    username = None
    name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(unique=True)
    avatar = models.ImageField(upload_to='avatars', blank=True, null=True)
    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def get_absolute_url(self):
        return reverse('users_user_url', kwargs={'id': self.id})
    
    def get_update_url(self):
        return reverse('users_update_url', kwargs={'id': self.id})
    
    def get_delete_url(self):
        return reverse('users_delete_url', kwargs={'id': self.id})
    
    def __str__(self):
        return f'{self.name}'