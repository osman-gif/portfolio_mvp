from django.shortcuts import render, redirect, get_object_or_404
from .models import SchoolProfile
from .forms import UpdateSchoolProfile
from posts.models import JobPost
import os

# View to display a school's profile
def school_profile(request, pk):
    """
    Displays the profile of a school.

    Args:
        request (HttpRequest): The request object.
        pk (int): The primary key of the school's user account.

    Returns:
        HttpResponse: Renders the school profile page with school details.
    """
    profile = SchoolProfile.objects.first()  # Adjust query as needed
    school = get_object_or_404(SchoolProfile, user=pk)  # Use get_object_or_404 for error handling
    posts = JobPost.objects.filter(school=school)
    return render(request, 'school/profile.html', {'school': school, 'posts':posts})


# View to update a school's profile
def update_profile(request, pk):
    """
    Handles updating a school's profile.

    Args:
        request (HttpRequest): The request object.
        pk (int): The primary key of the school's user account.

    Returns:
        HttpResponse: Renders the school profile update form, or redirects to the profile page upon successful update.
    """
    school_profile = get_object_or_404(SchoolProfile, user=pk)
    form = UpdateSchoolProfile(instance=school_profile)

    if request.method == 'POST':
        form = UpdateSchoolProfile(request.POST,request.FILES ,instance=school_profile)

        if form.is_valid():
            print(form.instance.image.url)
            school_profile = form.save(commit=False)  # Save without committing to assign the user
            school_profile.user = request.user  # Ensure the user is correctly assigned
            school_profile.save()  # Commit the save
            return redirect('school_profile', pk=pk)  # Redirect to the updated school profile page
        
    return render(request, 'school/update_school.html', {'form': form})

def delete_image(request, pk):
    school = get_object_or_404(SchoolProfile, id=pk)
    
    # Remove the image file from the filesystem
    if school.image:
        image_path = school.image.url
        if os.path.exists(image_path):
            os.remove(image_path)

    return render(request, 'school/delete_image.html')
    return redirect('home', pk=pk)