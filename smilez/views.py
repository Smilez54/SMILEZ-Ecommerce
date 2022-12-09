from django.shortcuts import render
from .models import Contact


# Create your views here.
def index(request):
    return render(request, 'index.html')


def cart(request):
    return render(request, 'cart.html')


def shop(request):
    return render(request, 'shop.html')


def checkout(request):
    return render(request, 'checkout.html')


def detail(request):
    return render(request, 'detail.html')


def contact(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        email = request.POST.get('email')
        message = request.POST.get('message')
        info = Contact(fname=fname, email=email, message=message)
        info.fname = fname
        info.email = email
        info.message = message
        info.save()
    return render(request, 'contact.html')
