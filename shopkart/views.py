from django.shortcuts import render, redirect

# Create your views here.
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def home(request):
    return render(request, "index.html")

def home(request):
    return render(request, "home.html")

@csrf_exempt
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'error': 'Invalid credentials'})
    return render(request, "login.html")


@csrf_exempt
def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            return JsonResponse({'success': False, 'error': 'Username already exists'})

        user = User.objects.create_user(username=username, email=email, password=password)
        auth_login(request, user)
        return JsonResponse({'success': True})
    return render(request, "signup.html")

def logout_view(request):
    logout(request)
    return redirect('home')