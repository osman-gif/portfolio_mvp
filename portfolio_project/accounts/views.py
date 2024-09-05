from django.shortcuts import render, redirect
from .forms import UserRgistrationForm
from .models import CustomUser
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.utils.crypto import get_random_string
from django.http import HttpResponseRedirect

# Create your views here.
 
def register(request):
    if request.method == 'POST':
        form = UserRgistrationForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('login')
    else:
        form = UserRgistrationForm()
    
    return render(request, 'accounts/register.html', {'form': form})

def users(request):
    users = CustomUser.objects.all()

    return render(request, 'accounts/users.html', {'users': users})



    return render(request, 'accounts/instructor_profile.html', {'instructors':instructors})

def login_view(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = CustomUser.objects.get(username=username)
        except:
            messages.error(request, "User Doesn't exist")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            session_key = get_random_string(32)
            request.session['session_key'] = session_key
            # Redirect to the dashboard with the session key in the URL
            return HttpResponseRedirect(f'/?session_key={session_key}')
            #return redirect(f'/?session_key={session_key}')
        else:
            messages.error(request, "User is not authenticated")
    context = {}
    return render(request, 'accounts/login_register.html', context)

def logout_view(request):
    logout(request)
    return redirect('home')

def delete_account(request, pk):
    account = CustomUser.objects.get(id=pk)

    account.delete()
    return redirect('register')