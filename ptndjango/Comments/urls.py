from django.urls import path
from .views import *

urlpatterns = [
    path('', CommentsHome.as_view(), name='comments_home_url'),
    path('commentsCreate/<str:postid>', CommentsCreate.as_view(), name='comments_create_url'),
    path('comemntsUpdate/<str:id>', CommentsUpdate.as_view(), name='comments_update_url'),
    path('commentsComment/<str:id>', CommentsComment.as_view(), name='comments_comment_url'),
]