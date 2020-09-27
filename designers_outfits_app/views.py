from django.shortcuts import render

def index(request):
    # retrieve info for the home page
    return render(request, 'index.html')

def NoResult(request):
    return render(request, '404.html')

def index_boxed(request):
    return render(request,'index-boxed.html')

def index_classic(request):
    return render(request,'index-classic.html')

def index_fashion(request):
    return render(request,'index-fashion.html')

def index_landing(request):
    return render(request,'index-landing.html')