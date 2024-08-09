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
    def create(connect, order: Order):
        # Вызвать запрос вставки данных из объекта в таблицу
        ...

    @staticmethod
    def read(connect) -> list[Order]:

        try:
            with connect.cursor() as cursor:

                query = """SELECT * 
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
        # Обновить данные о книге в таблице
        ...

    @staticmethod
    def delete(connect, order: Order):
        # Удалить девайс
        ...