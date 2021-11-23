from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    return render(request, 'hello.html', {'name': 'Yash'})

def index(request):
    return render(request, 'index.html')