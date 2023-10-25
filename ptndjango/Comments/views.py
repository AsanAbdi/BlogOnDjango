from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin


from .forms import *
from .models import Comment
from Posts.models import Post

# Create your views here.
class CommentsHome(View):
    def get(self, request):
        comments = Comment.objects.all()
        return render(request, 'commentsHome.html', {'comments': comments})
    
class CommentsComment(View):
    def get(self, request, id):
        comment = Comment.objects.get(id=id)
        return render(request, 'commentsComment.html', {'comment': comment})
    
class CommentsCreate(LoginRequiredMixin, View):
    def get(self, request, postid):
        form = CommentForm()
        post = Post.objects.get(id=postid)
        return render(request, 'commentsCreate.html', {'form': form, 'post': post})

    def post(self, request, postid):
        form = CommentForm(request.POST)
        post = Post.objects.get(id=postid)
        if form.is_valid():
            newComment = form.save(commit=False)
            newComment.user = request.user
            newComment.post = post
            newComment.save()
            return redirect(post)

class CommentsUpdate(LoginRequiredMixin, View):
    def get(self, request, id):
        comment = Comment.objects.get(id=id)
        form = UpdateCommentForm(instance=comment)
        return render(request, 'commentsUpdate.html', {'form': form, 'comment': comment})
    
    def post(self, request, id):
        comment = Comment.objects.get(id=id)
        form = UpdateCommentForm(request.POST, instance=comment)
        if form.is_valid():
            newComment = form.save()
            return redirect(newComment)