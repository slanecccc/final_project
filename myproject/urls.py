"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main.views import main
from order.views import order, send_order
from authorization.views import authorization, staff_authorization
from compilation.views import compilation
from staff.views import staff
urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', main),
    path('order/', order),
    path('authorization/', authorization),
    path('compilation/', compilation),
    path('order/send-order/', send_order),
    path('staff/', staff),
    path('authorization/send-staff/', staff_authorization),
]
