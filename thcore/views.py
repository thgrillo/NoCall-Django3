from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import MarkForm
from .models import *

# Create your views here.
def home(request):
    return render(request, 'thcore/home.html')

def loginPage(request): 
    return render(request, 'accounts/login.html')

@login_required
def send_data(request):
    if request.method == 'GET':
        form = MarkForm()
    else:
        form = MarkForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home/')
    context = {'form': form}
    return render(request, 'thcore/checkpg.html', context)
