from django.urls import path
from . import views
from application.views import application

urlpatterns = [
    path('instructors/<str:id>', views.instructor_profile, name='instructor_profile'),
    path('<str:id>/applications/', views.my_applications, name='my_applications'),
    path('application/<str:pk>/', application, name='application'),
]
