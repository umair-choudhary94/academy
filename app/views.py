from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from . models import *
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
import datetime
# Create your views here.
def home(request):
    return render(request,'home.html')




def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            
            login(request, user)
            
            return redirect('/dashboard')  
        else:
            
            error_message = 'Invalid username or password'
            return render(request, 'login.html', {'error_message': error_message})

    return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        pass
        # username = request.POST['email']
        # first_name = request.POST['name']
        # password1 = request.POST['password1']
        # password2 = request.POST['password2']
        # user_type = request.POST['user_type']

        # # Perform any additional validation or processing here
        
        # # Create a new user
        # user = User.objects.create_user(username=username, password=password1,first_name=first_name)
        
        # # Create a user profile
        # profile = UserProfile(user=user, role=user_type)
        # profile.save()
        
        # return redirect('login') 

       

    return render(request, 'signup.html')
def logout_view(request):
    logout(request)
    return redirect('home')

def pricing(request):
    return render(request,'pricing.html')
