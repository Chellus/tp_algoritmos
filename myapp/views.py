from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):  
    return HttpResponse("Index ")
def hello(request,user):
    print(user)
    return HttpResponse("Hello word")
def about(request):
    return HttpResponse('about')