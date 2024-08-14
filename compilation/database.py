from abc import ABC, abstractmethod
from .orders import Order, OrdersContainer
import psycopg2


class DBConnect:

    _instance = None

    @classmethod
    def get_connect(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = psycopg2.connect(*args, **kwargs)
        return cls._instance


class DBManager(ABC):

    @staticmethod
    @abstractmethod
    def create(connect, order: Order):
        ...

    @staticmethod
    @abstractmethod
    def read(connect, order: Order):
        ...

    @staticmethod
    @abstractmethod
    def update(connect, old_order: Order, new_order: Order):
        ...

    @staticmethod
    @abstractmethod
    def delete(connect, order: Order):
        ...


class PGOrdersManager(DBManager):

    @staticmethod
    def create(connect, order: Order) -> None:
        try:
            with connect.cursor() as cursor:
                params = (order.surname_client, order.name_client, order.patronymic_client, order.phone, order.city,
                          order.street, order.num_home, order.capacity, order.wight, order.height)
                query = """ 
                        INSERT INTO orders(surname_client, name_client, patronymic_client, phone_client, city, street, num_home, capacity, width, height)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                        
                        """
                cursor.execute(query, params)
        except (Exception, psycopg2.Error) as e:
            print(e)

    @staticmethod
    def read(connect) -> list[Order]:

        try:
            with connect.cursor() as cursor:

                query = """SELECT surname_client, name_client, patronymic_client, phone_client, city, street, num_home, capacity, width, height 
                           FROM orders
                        """
                cursor.execute(query)
                data = cursor.fetchall()

                if data:
                    container = OrdersContainer()
                    container.create_list_orders(data)
                    return container.get_list_orders()
                else:
                    raise Exception(f"Не найдена запись с параметрами")
        except (Exception, psycopg2.Error) as e:
            print(e)

    @staticmethod
    def update(connect, index_old_order: int, new_order: Order):
        # Обновить данные о заказе в таблице
        ...

    @staticmethod
    def delete(connect, order: Order):
        # Удалить заказ
        ...