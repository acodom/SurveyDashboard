from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('account')  # Redirect to dashboard or any other page after login
        else:
            # Handle invalid login
            return render(request, 'registration/login.html', {'error_message': 'Invalid username or password'})
    return render(request, 'registration/login.html')

def account(request):
    # Add logic to retrieve and display user profile information
    return render(request, 'registration/account.html')

def user_logout(request):
    logout(request)
    return redirect('login')  # Redirect to login page after logout
