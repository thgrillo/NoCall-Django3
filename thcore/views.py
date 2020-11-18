from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'thcore/home.html')

def login(request):   
    return render(request, 'registration/login.html')

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
    return render(request, 'webpage/checkpg.html', context)
