from django.urls import path
from . import views

urlpatterns = [
    path('<str:pk>/update_application/', views.update_application, name='update_application'),
    path('apply_to_post/', views.apply_to_post, name='apply_to_post'),
    path('applications_list/', views.applications_list, name='applications_list'),
    path('<str:job_post>/applications/', views.post_applications, name='post_applications'),
    path('application/<str:pk>/', views.application, name='application'),
    path('applicatin/<str:pk>/delete/', views.delete_application, name='delete_application')
]