from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from Users.models import User


from .models import Post
from .forms import *

# Create your views here.
class PostsHome(View):
    def get(self, request):
        posts = Post.objects.all()
        return render(request, 'postsHome.html', {'posts': posts})
    
class PostsPost(View):
    def get(self, request, id):
        post = Post.objects.get(id=id)
        return render(request, 'postsPost.html', {'post': post})

class PostsCreate(LoginRequiredMixin, View):
    def get(self, request):
        postForm = PostForm()
        return render(request, 'postsCreate.html', {'form': postForm})
    def post(self, request):
        postForm = PostForm(request.POST, request.FILES)
        print('errros', postForm.errors)
        if postForm.is_valid():
            newPost = postForm.save(commit=False) 
            newPost.user = request.user
            print('newpost', newPost)
            newPost.save()  
            return redirect(newPost)
        
class PostsUpdate(LoginRequiredMixin, View):
    def get(self, request, id):
        post = Post.objects.get(id=id)
        form = UpdatePostForm(instance=post)
        return render(request, 'postsUpdate.html', {'form': form, 'post': post})

    def post(self, request, id):
        post = Post.objects.get(id=id)
        form = UpdatePostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            newPost = form.save()
            return redirect(newPost)
        else:
            return render(request, 'postsUpdate.html', {'form': form, 'post': post})
        
class PostsDelete(LoginRequiredMixin, View):
    def get(self, request, id):
        post = Post.objects.get(id=id)
        return render(request, 'postsDelete.html', {'post': post})
    
    def post(self, request, id):
        post = Post.objects.get(id=id)
        post.delete()
        return redirect('posts_home_url')
    
class PostsLike(LoginRequiredMixin, View):
    def get(self, request, id):
        post = Post.objects.get(id=id)
        if request.user in post.likes.all():
            post.likes.remove(request.user.id)
        else:
            post.likes.add(request.user.id)
        return render(request, 'postsPost.html', {'post': post, 'likes': len(post.likes.all())})