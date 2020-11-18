from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import MarkForm

# Create your views here.
def home(request):
    return render(request, 'thcore/home.html')

def login(request):   
    return render(request, 'registration/login.html')

def send_data(request):
    return render(request, 'thcore/checkpg.html')




# @login_required
# def send_data(request):
#     if request.method == 'GET':
#         form = MarkForm()
#     else:
#         form = MarkForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/home/')
#     context = {'form': form}
#     return render(request, 'thcore/checkpg.html', context)
