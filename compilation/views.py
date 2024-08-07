from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

# Create your views here.
def compilation(request: HttpRequest):
    return render(request, 'compilation.html')