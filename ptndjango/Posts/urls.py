from django.urls import path
from .views import *

urlpatterns = [
    path('', PostsHome.as_view(), name='posts_home_url'),
    path('postsCreate', PostsCreate.as_view(), name='posts_create_url'),
    path('postsPost/<str:id>', PostsPost.as_view(), name='posts_post_url'),
    path('postsUpdate/<str:id>', PostsUpdate.as_view(), name='posts_update_url'),
    path('postsDelete/<str:id>', PostsDelete.as_view(), name='posts_delete_url'),
    path('postsLike/<str:id>', PostsLike.as_view(), name='posts_like_url')
]