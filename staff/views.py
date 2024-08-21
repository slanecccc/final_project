from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
# Create your views here.


def staff(request: HttpRequest):
    return render(request, 'staff.html')