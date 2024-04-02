from django.shortcuts import render, redirect
from django.contrib.auth import login,authenticate
from django.contrib import messages

from .forms import RegistrationForm,SignInForm

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_active = True
            user.save()
            return render(request, 'registration/login.html')  # Redirect to your home page after registration
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

def login_view(request):
    forms = SignInForm
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                link = request.GET.get('next')
                if link:
                    return redirect('date_selection') 
                return redirect('home')  # Replace 'home' with the URL of your home page
            else:
                messages.error(request, 'Invalid username or password')
    context = {"form": forms}
    return render(request, 'registration/login.html',context)