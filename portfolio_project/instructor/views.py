from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import InstructorProfile
from application.models import Application

@login_required(login_url='login')
def instructor_profile(request, id):
    """
    Renders the profile page of an instructor.

    Args:
        request (HttpRequest): The request object.
        id (int): The ID of the instructor's user account.

    Returns:
        HttpResponse: Renders the instructor's profile page with their data.
    """
    instructor = get_object_or_404(InstructorProfile, user=id)  # Use get_object_or_404 for better error handling
    return render(request, 'instructor/profile.html', {'instructor': instructor})

@login_required(login_url='login')
def my_applications(request, id):
    """
    Displays the applications submitted by the instructor.

    Args:
        request (HttpRequest): The request object.
        id (int): The ID of the instructor's user account.

    Returns:
        HttpResponse: Renders the applications page with a list of the instructor's applications.
    """
    instructor = get_object_or_404(InstructorProfile, user=id)
    my_applications = Application.objects.filter(instructor=instructor.user)  # Use the instructor instance for filtering

    return render(request, 'instructor/my_applications.html', {
        'my_applications': my_applications,
        'instructor': instructor
    })
