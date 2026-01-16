from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm, CreateRecordForm
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'web/index.html')

def register(request):
    form = CreateUserForm(request.POST)
    if request.method == 'POST':
        form.save()
    else:
        form = CreateUserForm()
    
    context = {'form': form}

    return render(request, 'web/register.html', context)


def login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request,  username=username, password=password)

            if user is not None:
                auth_login(request, user)
                return redirect('dashboard')

    else:
        form = LoginForm()

    context = {'form': form}

    return render(request, 'web/login.html', context)

@login_required(login_url='login')
def dashboard(request):
    return render(request, 'web/dashboard.html')


def logout(request):
    auth_logout(request)
    return redirect('login')


@login_required(login_url='login')
def create_record(request):
    form = CreateRecordForm()
    if request.method == 'POST':
        form = CreateRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = CreateRecordForm()
    
    context = {'form': form}

    return render(request, 'web/create-record.html', context)
        