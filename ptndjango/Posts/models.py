from django.db import models
from Users.models import User
from Categories.models import Category
from datetime import datetime
from django.shortcuts import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=1000000)
    date_pub = models.DateTimeField(default=datetime.now)
    photo = models.ImageField(upload_to='postPhotos')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='userposts')
    likes = models.ManyToManyField(User, blank=True, related_name='likeposts')
    category = models.ForeignKey(Category, blank=True, related_name='categoryposts', on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('posts_post_url', kwargs={'id': self.id})
    
    def get_update_url(self):
        return reverse('posts_update_url', kwargs={'id': self.id})
    
    def get_delete_url(self):
        return reverse('posts_delete_url', kwargs={'id': self.id})
    
    def __str__(self):
        return f'{self.title}'
    
    