from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm  
from django.shortcuts import redirect 
from django import forms


# Create your views here.

def index(request):
    return render (request,"index.html")

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request,'register/registration.html', {'form': form})
    


