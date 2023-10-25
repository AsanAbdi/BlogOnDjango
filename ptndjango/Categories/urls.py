from django.urls import path

from .views import *

urlpatterns = [
    path('', CategoriesHome.as_view(), name='categories_home_url'),
    path('categoriesCreate', CategoriesCreate.as_view(), name='categories_create_url'),
    path('categoryCategory/<str:id>', CategoriesCategory.as_view(), name='categories_category_url'),
    path('categoriesUpdate/<str:id>', CategoriesUpdate.as_view(), name='categories_update_url'),
    path('categoriesDelete/<str:id>', CategoriesDelete.as_view(), name='categories_delete_url')
]