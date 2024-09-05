from django.shortcuts import render, redirect
from posts.views import posts
from posts.models import JobPost
from django.db.models import Q
from accounts.models import CustomUser
from application.models import Application

def home(request):
    posts = None
    subjects = None
    applications = None
    subjects = JobPost.objects.all()

    #filter posts according to subjects
    q = request.GET.get('q')
    if q:
        posts = JobPost.objects.filter(Q(subject__icontains=q) | 
                                           Q(employment_type__icontains=q))
    else:
        posts = JobPost.objects.all()

    #check the type of user
    if request.user.is_authenticated:
        if request.user.user_type == 'instructor':
            q = request.GET.get('q')
            subjects = ['math', 'english', 'ict']
        
        else:
            applications = None
            q = request.GET.get('q')

            if q:
                #fliter applications according to postition
                applications = Application.objects.filter(Q(job_post=q))
            else:
                applications = Application.objects.all()

    return render (request, 'home.html', {'posts':posts, 'applications':applications, 'subjects':subjects})

