from django.shortcuts import render
from django.db.models import Q
from posts.models import JobPost
from application.models import Application
from django.shortcuts import get_object_or_404, redirect
from school.models import SchoolProfile
import os

def home(request):
    """
    View for the home page, displaying job posts and, for authenticated users,
    their related applications (for schools) or subject-specific posts (for instructors).
    
    - If a search query is provided via the 'q' parameter, it filters job posts and applications
      based on the search.
    - For instructors, predefined subjects are shown for browsing posts.
    - For schools, relevant job applications are displayed.

    Args:
        request: The HTTP request object.

    Returns:
        Renders the 'home.html' template with a context containing:
        - posts: The job posts, filtered by search query or all posts.
        - applications: The applications for authenticated users (schools).
        - subjects: A list of distinct subjects for filtering job posts.
    """

    # Get search query from the request
    query = request.GET.get('q', '')

    # Filter job posts based on the query (subject or employment type), or get all if no query
    if query:
        posts = JobPost.objects.filter(
            Q(subject__icontains=query) | Q(employment_type__icontains=query)
        )
    else:
        posts = JobPost.objects.all()

    # Get distinct subjects for filtering job posts
    subjects = JobPost.objects.values_list('subject', flat=True).distinct()

    # Initialize applications to None
    applications = None

    # Handle authenticated users
    if request.user.is_authenticated:
        if request.user.user_type == 'instructor':
            # If the user is an instructor, show predefined subjects
            subjects = ['math', 'english', 'ict']
        else:
            # If the user is a school, filter applications by job post subject or show all applications
            if query:
                applications = Application.objects.filter(
                    Q(job_post__subject__icontains=query)
                )
            else:
                applications = Application.objects.all()

    # Prepare the context to pass to the template
    context = {
        'school': request.user,
        'posts': posts,           # Job posts filtered by the search query
        'applications': applications,  # Applications for schools (None for instructors)
        'subjects': subjects,     # List of subjects for filtering job posts
    }

    # Render the 'home.html' template with the context
    return render(request, 'home.html', context)

