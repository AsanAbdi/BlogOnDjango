from django.db import models
from django.shortcuts import reverse

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=50, unique=True)

    def get_absolute_url(self):
        return reverse('categories_category_url', kwargs={'id': self.id})
    
    def get_update_url(self):
        return reverse('categories_update_url', kwargs={'id': self.id})
    
    def get_delete_url(self):
        return reverse('categories_delete_url', kwargs={'id': self.id})
    
    def __str__(self):
        return f'{self.title}'