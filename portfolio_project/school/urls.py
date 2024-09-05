from django.urls import path
from .views import SchoolProfile
from . import views

urlpatterns = [
    path('school/<str:pk>', views.school_profile, name='school_profile'),
    path('update_school_profile/<str:pk>',views.update_profile, name='update_school_profile' )
]