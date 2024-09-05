from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.register, name='register'),
    path('users/', views.users, name='users'),
    path('login', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('delete_account/<str:pk>', views.delete_account,name='delete_account'),
]