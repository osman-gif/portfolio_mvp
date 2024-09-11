from django.shortcuts import render, redirect
from .models import InstructorProfile
from application.models import Application
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def instructor_profile(request, id):
    instructor = InstructorProfile.objects.get(user=id)
    
    return render(request, 'instructor/profile.html', {'instructor':instructor})


def my_applications(request, id):
    my_applications = Application.objects.filter(instructor=id)

    return render(request, 'instructor/my_applications.html', {'my_applications':my_applications})