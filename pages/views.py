from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from django.db import IntegrityError
from django.contrib.auth import authenticate, login
from .models import TeachingAssistant
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import TeachingAssistant
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


def home(request):
    teaching_assistants = TeachingAssistant.objects.all()
    return render(request, 'pages/home.html', {'teaching_assistants': teaching_assistants})



def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_superuser:
                login(request, user)
                if not request.GET.get('next'):
                    return redirect('adminHome')
            else:
                error_message = "Invalid Username or Password"
        else:
            error_message = "Invalid Username or Password"
    else:
        error_message = None

    return render(request, 'pages/login.html', {'error_message': error_message})

def adminHome(request):
    teaching_assistants = TeachingAssistant.objects.all()
    return render(request, 'pages/adminHome.html', {'teaching_assistants': teaching_assistants})

def createUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        auth_code = request.POST.get('auth_code')
        
        # Check if the authentication code is correct
        if auth_code != 'clark':
            return render(request, 'pages/createUser.html', {'error_message': 'Invalid authentication code. Please try again.'})
        
        try:
            # Check if the username already exists
            if User.objects.filter(username=username).exists():
                return render(request, 'pages/createUser.html', {'error_message': 'Username already exists. Please choose a different one.'})
            
            # Create the superuser
            user = User.objects.create_superuser(username=username, email=email, password=password)
            return redirect('adminHome')  # Redirect to adminHome.html on successful creation
        except IntegrityError:
            return render(request, 'pages/createUser.html', {'error_message': 'An error occurred while creating the superuser. Please try again.'})
    
    return render(request, 'pages/createUser.html')

def hours(request):
    teaching_assistants = TeachingAssistant.objects.all()
    return render(request, 'pages/hours.html', {'teaching_assistants': teaching_assistants})



def delete_teaching_assistant(request, pk):
    teaching_assistant = get_object_or_404(TeachingAssistant, pk=pk)
    teaching_assistant.delete()
    return redirect('hours')