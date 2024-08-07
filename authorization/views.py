from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
# Create your views here.

def authorization(request: HttpRequest):
    return render(request, 'authorization.html')