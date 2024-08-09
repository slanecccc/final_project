from abc import ABC, abstractmethod


class Order:

    def __init__(self):
        self.num_order = None
        self.surname_client = None
        self.name_client = None
        self.patronymic_client = None
        self.phone = None
        self.city = None
        self.street = None
        self.num_home = None
        self.capacity = None
        self.wight = None
        self.height = None


class Builder(ABC):

    @abstractmethod
    def create(self):
        ...

    @abstractmethod
    def set_num_order(self, num_order):
        ...

    @abstractmethod
    def set_surname_client(self, surname_client):
        ...

    @abstractmethod
    def set_name_client(self, name_client):
        ...

    @abstractmethod
    def set_patronymic_client(self, patronymic_client):
        ...

    @abstractmethod
    def set_phone(self, phone):
        ...

    @abstractmethod
    def set_city(self, city):
        ...

    @abstractmethod
    def set_street(self, street):
        ...

    @abstractmethod
    def set_num_home(self, num_home):
        ...

    @abstractmethod
    def set_capacity(self, capacity):
        ...

    @abstractmethod
    def set_wight(self, wight):
        ...

    @abstractmethod
    def set_height(self, height):
        ...

    @abstractmethod
    def get_order(self):
        ...


class OrderBuilder(Builder):
    _order: Order

    def create(self):
        self._order = Order()

    def set_num_order(self, num_order):
        self._order.num_order = num_order

    def set_surname_client(self, surname_client):
        self._order.surname_client = surname_client

    def set_name_client(self, name_client):
        self._order.name_client = name_client

    def set_patronymic_client(self, patronymic_client):
        self._order.patronymic_client = patronymic_client

    def set_phone(self, phone):
        self._order.phone = phone

    def set_city(self, city):
        self._order.city = city

    def set_street(self, street):
        self._order.street = street

    def set_num_home(self, num_home):
        self._order.num_home = num_home

    def set_capacity(self, capacity):
        self._order.capacity = capacity

    def set_wight(self, wight):
        self._order.wight = wight

    def set_height(self, height):
        self._order.height = height

    def get_order(self):
        return self._order


class OrderCreator:

    def __init__(self, builder: Builder):
        self._builder = builder

    def change_builder(self, builder: Builder):
        self._builder = builder

    def make(self, order: tuple) -> Order:
        self._builder.create()
        self._builder.set_num_order(order[0])
        self._builder.set_surname_client(order[1])
        self._builder.set_name_client(order[2])
        self._builder.set_patronymic_client(order[3])
        self._builder.set_phone(order[4])
        self._builder.set_city(order[5])
        self._builder.set_street(order[6])
        self._builder.set_num_home(order[7])
        self._builder.set_capacity(order[8])
        self._builder.set_wight(order[9])
        self._builder.set_height(order[10])
        return self._builder.get_order()


class OrdersContainer:

    def __init__(self):
        self._orders: list[Order] = []

    def create_list_orders(self, data: list) -> None:
        builder = OrderBuilder()
        creator = OrderCreator(builder)

        for record in data:
            order = creator.make(record)
            self._orders.append(order)

    def add_order(self, order: Order):
        self._orders.append(order)

    def get_list_orders(self):
        return self._orders