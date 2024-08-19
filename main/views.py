from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from compilation.database import DBConnect, PGOrdersManager

# Create your views here.
def main(request: HttpRequest):
    connect = DBConnect.get_connect(dbname='final_project',
                                    host='localhost',
                                    port=5432,
                                    user='postgres',
                                    password='postgres')

    cars_min = PGOrdersManager.num_car_min(connect)
    cars_mid = PGOrdersManager.num_car_mid(connect)
    cars_max = PGOrdersManager.num_car_max(connect)

    context = {
        "cars_min": cars_min,
        "cars_mid": cars_mid,
        "cars_max": cars_max,
    }

    return render(request, 'main.html', context=context)

