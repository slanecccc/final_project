from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from compilation.orders import OrderCreator, OrderBuilder
from compilation.database import DBConnect, PGOrdersManager

# Create your views here.


def order(request: HttpRequest):
    return render(request, 'order.html')


def send_order(request: HttpRequest):
    connect = DBConnect.get_connect(dbname='final_project',
                                    host='localhost',
                                    port=5432,
                                    user='postgres',
                                    password='postgres')
    if request.method == "POST":
        surname = request.POST.get('surname', '')
        name_client = request.POST.get('name', '')
        patronymic_client = request.POST.get('patronymic', '')
        phone_client = request.POST.get('phone', '')
        city = request.POST.get('city', '')
        street = request.POST.get('street', '')
        num_house = request.POST.get('house', '')
        capacity = request.POST.get('capacity', '')
        width = request.POST.get('width', '')
        height = request.POST.get('height', '')

        params_order = (surname, name_client, patronymic_client, phone_client, city,
                        street, num_house, capacity, width, height)
        order_builder = OrderBuilder()
        order = OrderCreator(order_builder)
        make_order = order.make(params_order)
        PGOrdersManager.create(connect, make_order)
        connect.commit()
    return render(request, 'main.html')