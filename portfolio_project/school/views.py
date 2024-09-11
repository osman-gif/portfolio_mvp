from django.shortcuts import render, redirect
from .models import SchoolProfile
from .forms import UpdateSchoolProfile

# Create your views here.

def school_profile(request, pk):

    school = SchoolProfile.objects.get(user=pk)
    

    return render(request, 'school/profile.html', {'school':school})

def update_profile(request, pk):
    school_profile = SchoolProfile.objects.get(user=pk)
    form = UpdateSchoolProfile(instance=school_profile)

    if request.method == 'POST':
        form = UpdateSchoolProfile(request.POST, instance=school_profile)

        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            return redirect('school_profile',pk)
        
    return render(request, 'school/update_school.html', {'form':form})