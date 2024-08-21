from abc import ABC, abstractmethod


class Data:

    def __init__(self):
        self.login = None
        self.password = None


class Builder(ABC):

    @abstractmethod
    def create(self):
        ...

    @abstractmethod
    def set_login(self, login):
        ...

    @abstractmethod
    def set_password(self, password):
        ...

    @abstractmethod
    def get_data(self):
        ...

class DataBuilder(Builder):
    _data: Data

    def create(self):
        self._data = Data()

    def set_login(self, login):
        self._data.login = login

    def set_password(self, password):
        self._data.password = password

    def get_data(self):
        return self._data


class DataCreator:

    def __init__(self, builder: Builder):
        self._builder = builder

    def change_builder(self, builder: Builder):
        self._builder = builder

    def make(self, data: tuple) -> Data:
        self._builder.create()
        self._builder.set_login(data[0])
        self._builder.set_password(data[1])
        return self._builder.get_data()


class DataContainer:

    def __init__(self):
        self._data: list[Data] = []

    def create_list_data(self, data: list) -> None:
        builder = DataBuilder()
        creator = DataCreator(builder)

        for record in data:
            data_staff = creator.make(record)
            self._data.append(data_staff)

    def add_data(self, data: Data):
        self._data.append(data)

    def get_list_data(self):
        return self._data