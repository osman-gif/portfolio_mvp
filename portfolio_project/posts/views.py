from django.shortcuts import render, redirect
from .models import JobPost
from .forms import PostForm
from application.models import Application
from django.contrib.auth.decorators import login_required

# Create your views here.

def create_post(request):
    # posts = JobPost.objects.all()
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts')
    return render(request, 'posts/create_post.html', {'form': form})

def update_post(request, pk):
    post = JobPost.objects.get(id=pk)
    form = PostForm(instance=post)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'posts/update_post.html', {'form':form})

@login_required(login_url='login')
def delete_post(request, id):
    post = JobPost.objects.get(id=id)
    if request.method == 'POST':
        post.delete()
        return redirect('home')
    return render(request, 'posts/delete.html', {'instance': post})

def get_applications(post):
    applications = Application.objects.filter(job_post=post)
    return applications

@login_required(login_url='login')
def posts(request):
    post_applications = {}
    posts = JobPost.objects.all()

    for post in posts:
        #get all post applications
        applications = get_applications(post)
        post_applications[post] = applications


    return render(request, 'posts/posts.html', {'posts':posts, 'post_applications': post_applications})

@login_required(login_url='login')
def post(request, id):
    post = JobPost.objects.get(id=id)
    applications =  Application.objects.filter(job_post=id)
    applied = False
    application = None

    for application in applications:
        if application.instructor == request.user:
            applied = True
            application = Application.objects.get(instructor=request.user)
    return render(request, 'posts/current_post.html', {'post':post, 'applications':applications, 'applied':applied, 'application':application})
