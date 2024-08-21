from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from authorization.base_authorization import DBConnect, PGODataManager
# Create your views here.

def authorization(request: HttpRequest):

    return render(request, 'authorization.html')


def staff_authorization(request: HttpRequest):
    global context
    connect = DBConnect.get_connect(dbname='final_project',
                                    host='localhost',
                                    port=5432,
                                    user='postgres',
                                    password='postgres')

    if request.method == "POST":
        login = request.POST.get('login', '')
        password = request.POST.get('password', '')

        data_staff = (login, password)

        data = PGODataManager.read(connect, data_staff)
        if data:
            return render(request, 'staff.html')



