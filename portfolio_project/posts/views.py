from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import JobPost
from .forms import PostForm
from application.models import Application

# View to create a new job post
def create_post(request):
    """
    Handles the creation of a new job post.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: Renders the job post creation form, or redirects to 'posts' upon successful submission.
    """
    form = PostForm()

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts')  # Redirect to the posts listing page after saving the form
    
    return render(request, 'posts/create_post.html', {'form': form})


# View to update an existing job post
def update_post(request, pk):
    """
    Handles updating an existing job post.

    Args:
        request (HttpRequest): The request object.
        pk (int): The primary key of the job post to update.

    Returns:
        HttpResponse: Renders the job post update form, or redirects to 'home' upon successful update.
    """
    post = get_object_or_404(JobPost, id=pk)
    form = PostForm(instance=post)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to the homepage after successful update
    
    return render(request, 'posts/update_post.html', {'form': form})


# View to delete a job post
@login_required(login_url='login')
def delete_post(request, id):
    """
    Handles deleting a job post.

    Args:
        request (HttpRequest): The request object.
        id (int): The ID of the job post to delete.

    Returns:
        HttpResponse: Renders the delete confirmation page, or redirects to 'home' after deletion.
    """
    post = get_object_or_404(JobPost, id=id)

    if request.method == 'POST':
        post.delete()
        return redirect('home')  # Redirect to the homepage after successful deletion
    
    return render(request, 'posts/delete.html', {'instance': post})


# Helper function to get applications for a given job post
def get_applications(post):
    """
    Retrieves all applications related to a specific job post.

    Args:
        post (JobPost): The job post for which to retrieve applications.

    Returns:
        QuerySet: A queryset of applications related to the job post.
    """
    return Application.objects.filter(job_post=post)


# View to list all job posts and their associated applications
@login_required(login_url='login')
def posts(request):
    """
    Displays a list of all job posts along with their associated applications.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: Renders the posts listing page with job posts and their applications.
    """
    post_applications = {}
    posts = JobPost.objects.all()

    for post in posts:
        applications = get_applications(post)  # Get all applications for each post
        post_applications[post] = applications

    return render(request, 'posts/posts.html', {'posts': posts, 'post_applications': post_applications})


# View to display a specific job post and its applications
@login_required(login_url='login')
def post(request, id):
    """
    Displays the details of a specific job post along with its applications.

    Args:
        request (HttpRequest): The request object.
        id (int): The ID of the job post to display.

    Returns:
        HttpResponse: Renders the details of the job post and its applications, with information on whether the user has applied.
    """
    post = get_object_or_404(JobPost, id=id)
    applications = Application.objects.filter(job_post=id)
    applied = False
    application = None

    for app in applications:
        if app.instructor == request.user:
            applied = True
            application = app  # Set the user's application if they have applied
    
    return render(request, 'posts/current_post.html', {
        'post': post,
        'applications': applications,
        'applied': applied,
        'application': application
    })
