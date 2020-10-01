from django.shortcuts import render
import requests

def not_found(request):
    return render(request, '404.html')

def blog_landing(request):
    return render(request,'blog_landing.html')

def product(request,id):
    url = "https://asos2.p.rapidapi.com/products/v3/detail"
    querystring = {"store":"US","sizeSchema":"US","lang":"en-US","currency":"USD","id":id}
    headers = {
    'x-rapidapi-host': "asos2.p.rapidapi.com",
    'x-rapidapi-key': "47e36b370fmsh4437be8672c0154p1c0cb8jsn42ab70fa5204"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    images = []
    for i in response.json()['media']['images']:
        images.append(i['url'])
    context = {
        "name" : response.json()['name'],
        "des" : response.json()['description'],
        "brand" : response.json()['brand']['name'],
        "sizeGuide" : response.json()['sizeGuide'],
        "variants" : response.json()['variants'],
        "images" : images,
        "info" : response.json()['info'],
        "baseURL" : response.json()['baseUrl'],
    }
    return render(request,'product.html',context)

# def product(request,id):
#     return render(request,'product.html')

def index_fashion(request):
    return render(request,'index-fashion.html')

def index_landing(request):
    return render(request,'index-landing.html')

