from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserRgistrationForm
from .models import CustomUser
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.utils.crypto import get_random_string
from django.http import HttpResponseRedirect

# Handles user registration. Displays the registration form and processes form submissions.
def register(request):
    if request.method == 'POST':
        form = UserRgistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to the login page after successful registration
            return redirect('login')
    else:
        # Display an empty form for GET requests
        form = UserRgistrationForm()
    
    return render(request, 'accounts/register.html', {'form': form})

# Displays a list of all users. Requires authentication or further access control.
def users(request):
    # Fetch all registered users
    users = CustomUser.objects.all()

    return render(request, 'accounts/users.html', {'users': users})

# Handles user login. Validates credentials and logs in the user if authenticated.
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            # Check if the user exists in the system
            user = CustomUser.objects.get(username=username)
        except CustomUser.DoesNotExist:
            messages.error(request, "User doesn't exist")
            return redirect('login')

        # Authenticate the user with the provided credentials
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Log the user in and generate a session key
            login(request, user)
            session_key = get_random_string(32)
            request.session['session_key'] = session_key
            # Redirect to the home page with the session key in the URL
            return HttpResponseRedirect(f'/?session_key={session_key}')
        else:
            # Display error message for invalid credentials
            messages.error(request, "Invalid username or password")
    
    return render(request, 'accounts/login_register.html')

# Logs the user out and redirects to the home page.
def logout_view(request):
    logout(request)
    return redirect('home')

# Deletes a user's account by primary key (id). Once deleted, redirects to the registration page.
def delete_account(request, pk):
    # Fetch the specific account to delete
    account = get_object_or_404(CustomUser, id=pk)

    # Delete the account and redirect to the registration page
    account.delete()
    return redirect('register')
