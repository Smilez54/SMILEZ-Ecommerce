from django.shortcuts import render
from . import views

# Create your views here.
def register(request):
    return render(request, 'register.html')

