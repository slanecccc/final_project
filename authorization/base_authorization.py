from abc import ABC, abstractmethod
from .data_authorization import Data, DataContainer
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
    def create(connect, data: Data):
        ...

    @staticmethod
    @abstractmethod
    def read(connect, data_staff: tuple):
        ...


    @staticmethod
    @abstractmethod
    def delete(connect, data: Data):
        ...


class PGODataManager(DBManager):

    @staticmethod
    def create(connect, data: Data) -> None:
        ...

    @staticmethod
    def read(connect, data_staff: tuple) -> list[Data]:

        try:
            with connect.cursor() as cursor:
                params = (data_staff[0], data_staff[1])
                query = """
                        SELECT login_staff, password_staff
                        FROM staff
                        WHERE login_staff = %s AND password_staff = %s
                        
                        """
                cursor.execute(query, params)
                data = cursor.fetchall()

                if data:
                    container = DataContainer()
                    container.create_list_data(data)
                    return container.get_list_data()
                else:
                    raise Exception(f"Такого пользователь не существует")
        except (Exception, psycopg2.Error) as e:
            print(e)
