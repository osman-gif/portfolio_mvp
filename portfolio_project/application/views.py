from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ApplicationForm
from .models import Application
from posts.models import JobPost

# Apply for a job post. The view requires the user to be authenticated.
# It displays the application form and handles form submission.
@login_required(login_url='login')
def apply_to_post(request):
    # Initialize an empty form
    form = ApplicationForm()

    # Check if the request method is POST (form submission)
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            # Save the form and redirect to home if valid
            form.save()
            return redirect('home')

    # Render the application form page
    return render(request, 'application/application_form.html', {'form': form})

# Display a list of all applications. Requires authentication.
@login_required(login_url='login')
def applications_list(request):
    # Fetch all application objects
    applications = Application.objects.all()
    context = {'applications': applications}

    # Render the application list page
    return render(request, 'application/application_list.html', context)

# View all applications for a specific job post. Requires authentication.
@login_required(login_url='login')
def post_applications(request, job_post):
    # Fetch applications related to a specific job post
    applications_list = Application.objects.filter(job_post=job_post)

    context = {'applications': applications_list}

    # Render the post-specific applications page
    return render(request, 'application/post_applications.html', context)

# Delete an application by its primary key (id). Requires authentication.
# Confirms deletion via POST request.
@login_required(login_url='login')
def delete_application(request, pk):
    # Fetch the specific application to delete
    application = get_object_or_404(Application, id=pk)

    # Handle POST request for deleting the application
    if request.method == 'POST':
        application.delete()
        return redirect('home')

    # Render the delete confirmation page
    return render(request, 'delete.html', {'instance': application})

# Update an existing application by its primary key (id). Requires authentication.
# Loads an update form prefilled with the application's current data.
@login_required(login_url='login')
def update_application(request, pk):
    # Fetch the specific application to update
    application = get_object_or_404(Application, id=pk)

    # Prepopulate the form with the application data
    form = ApplicationForm(instance=application)

    # Handle form submission
    if request.method == 'POST':
        form = ApplicationForm(request.POST, instance=application)
        if form.is_valid():
            # Save changes and redirect to home
            form.save()
            return redirect('home')

    # Render the application update form page
    return render(request, 'application/update_application.html', {'form': form})

# View a specific application by its primary key (id). Requires authentication.
@login_required(login_url='login')
def application(request, pk):
    # Fetch the specific application
    application = get_object_or_404(Application, id=pk)

    # Render the application details page
    return render(request, 'application/application.html', {'application': application})
