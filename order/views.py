from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
# Create your views here.


def order(request: HttpRequest):
    return render(request, 'order.html')