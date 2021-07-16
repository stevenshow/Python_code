from django.shortcuts import render

# Create your views here.

def index(request, *argts, **kwargs):
    return render(request, 'frontend/index.html')
