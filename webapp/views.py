from django.shortcuts import render
from .forms import CreateUserForm

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