from django.shortcuts import render
from .models import *
# Create your views here.


def index(request):
    return render(request,'index.html')


def display_one(request):
    items = One.objects.all()
    context={
        'items': items,
        'header': 'ONE'
    }
    return render(request, 'index.html',context)


def display_two(request):
    items = Two.objects.all()
    context={
        'items': items,
        'header': 'TWO'
    }
    return render(request, 'index.html',context)