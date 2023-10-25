from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Category
from .forms import *

# Create your views here.
class CategoriesHome(View):
    def get(self, request):
        ctgr = Category.objects.all()
        return render(request, 'categoriesHome.html', {'categories': ctgr})
    
class CategoriesCreate(LoginRequiredMixin, View):
    def get(self, request):
        form = CategoryForm()
        return render(request, 'categoriesCreate.html', {'form': form})

    def post(self, request):
        form = CategoryForm(request.POST)
        if form.is_valid():
            newCategory = form.save()
            return redirect(newCategory)
        else:
            return render(request, 'categoriesCreate.html', {'form': form})
        
class CategoriesUpdate(LoginRequiredMixin, View):
    def get(self, request, id):
        category = Category.objects.get(id=id)
        form = UpdateCategoryForm(instance=category)
        return render(request, 'categoriesUpdate.html', {'form':form, 'category': category})
    def post(self, request, id):
        category = Category.objects.get(id=id)
        form = UpdateCategoryForm(request.POST, instance=category)
        if form.is_valid():
            UpdatedCategory = form.save()
            return redirect(UpdatedCategory)

class CategoriesCategory(View):
    def get(self, request, id):
        category = Category.objects.get(id=id)
        return render(request, 'categoriesCategory.html', {'category': category})
    
class CategoriesDelete(LoginRequiredMixin, View):
    def get(self, request, id):
        category = Category.objects.get(id=id)
        return render(request, 'categoriesDelete.html', {'category': category})
    
    def post(self, request, id):
        category = Category.objects.get(id=id)
        category.delete()
        return redirect('categories_home_url')
