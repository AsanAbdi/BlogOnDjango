from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from .views import *

urlpatterns = [
    path('', UsersHome.as_view(), name='users_home_url'),
    path('usersCreate', UsersCreate.as_view(), name='users_create_url'),
    path('UserUpdate/<str:id>', UsersUpdate.as_view(), name='users_update_url'),
    path('usersUser/<str:id>', UsersUser.as_view(), name='users_user_url'),
    path('usersDelete/<str:id>', UsersDelete.as_view(), name='users_delete_url'),
    path('usersLogin', UsersLogin.as_view(), name='users_login_url'),
    path('usersLogout', UsersLogout.as_view(), name='users_logout_url')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)