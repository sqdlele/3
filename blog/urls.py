from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.article_list, name='article_list'),
    path('search/', views.article_search, name='article_search'),
    path('article/create/', views.article_create, name='article_create'),
    path('article/<int:pk>/', views.article_detail, name='article_detail'),
    path('article/<int:pk>/edit/', views.article_update, name='article_update'),
    path('article/<int:pk>/delete/', views.article_delete, name='article_delete'),
    path('categories/', views.category_list, name='category_list'),
    path('categories/create/', views.category_create, name='category_create'),
    path('categories/<int:pk>/edit/', views.category_update, name='category_update'),
    path('categories/<int:pk>/delete/', views.category_delete, name='category_delete'),
    path('tags/', views.tag_list, name='tag_list'),
    path('tags/create/', views.tag_create, name='tag_create'),
    path('tags/<int:pk>/edit/', views.tag_update, name='tag_update'),
    path('tags/<int:pk>/delete/', views.tag_delete, name='tag_delete'),
] 