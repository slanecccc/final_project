from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from compilation.orders import Order, OrderBuilder, OrdersContainer
from compilation.database import DBConnect, PGOrdersManager


# Create your views here.
def compilation(request: HttpRequest):
    connect = DBConnect.get_connect(dbname='final_project',
                                    host='localhost',
                                    port=5432,
                                    user='postgres',
                                    password='postgres')

    data = PGOrdersManager.read(connect)

    context = {
        "data": data,
    }

    return render(request, template_name='compilation.html', context=context)
