from django.shortcuts import reverse
from django.db import models
from Users .models import User
from Posts.models import Post

# Create your models here.
class Comment(models.Model):
    text = models.CharField(max_length=100000)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usercomments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='postcomments')

    def get_absolute_url(self):
        return reverse('comments_comment_url', kwargs={'id': self.id})
    
    def get_update_url(self):
        return reverse('comments_update_url', kwargs={'id': self.id})
    
    def __str__(self):
        return f'{self.text}'