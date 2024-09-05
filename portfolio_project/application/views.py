from django.shortcuts import render, redirect
from .forms import ApplicationForm
from .models import Application
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='login')
def apply_to_post(request):
    form = ApplicationForm()

    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    return render(request, 'application/application_form.html', {'form': form})

@login_required(login_url='login')
def applications_list(request):
    applications = Application.objects.all()
    context = {'applications': applications}

    return render(request, 'application/application_list.html', context)

@login_required(login_url='login')
def post_applications(request, job_post):
    applications_list = Application.objects.filter(job_post=job_post)

    context = {'applications': applications_list}
    return render(request, 'application/post_applications.html', context)

@login_required(login_url='login')
def delete_application(request, pk):
    application = Application.objects.get(id=pk)
    if request.method == 'POST':
        application.delete()
        return redirect('home')
    return render(request, 'delete.html', {'instance':application})

@login_required(login_url='login')
def update_application(request, pk):
     application = Application.objects.get(id=pk)
     form = ApplicationForm(instance=application)
     
     if request.method == 'POST':
         form = ApplicationForm(request.POST, instance=application)
         
         if form.is_valid():
             form.save()
             return redirect('home')
     return render(request, 'application/update_application.html', {'form':form})


@login_required(login_url='login')
def application(request, pk):

    application = Application.objects.get(id=pk)

    return render(request, 'application/application.html', {'application':application})