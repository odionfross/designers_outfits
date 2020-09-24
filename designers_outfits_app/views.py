from django.shortcuts import render

def index(request):
    # retrieve info for the home page
    return render(request, 'index-fashion.html')

def NoResult(request):
    return render(request, '404.html')