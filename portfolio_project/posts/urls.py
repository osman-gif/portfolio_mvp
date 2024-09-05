from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('create_post/', views.create_post, name='create_post'),
    path('update_post/<str:pk>', views.update_post, name='update_post'),
    path('posts/', views.posts, name='posts'),
    path('post/<str:id>/', views.post, name='current_post'),
    path('delete/<str:id>/', views.delete_post, name='delete_post'),
]
