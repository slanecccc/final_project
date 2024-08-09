from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from compilation.orders import Order, OrderBuilder, OrdersContainer
from compilation.database import DBConnect, PGOrdersManager
# Create your views here.


# def compilation(request: HttpRequest):
#     return render(request, 'compilation.html')


def compilation(request: HttpRequest):
    connect = DBConnect.get_connect(dbname='final_project',
                                    host='localhost',
                                    port=5432,
                                    user='postgres',
                                    password='postgres')

    # cursor = connect.cursor()
    # query = """ SELECT * FROM orders """
    # cursor.execute(query)
    # container = OrdersContainer()
    # container.create_list_orders(cursor.fetchall())
    data = PGOrdersManager.read(connect)
    # count = len(data) if data is not None else 0

    context = {
        "data": data,
    }

    return render(request, template_name='compilation.html', context=context)

