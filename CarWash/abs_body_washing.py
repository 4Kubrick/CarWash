from abc import ABC, abstractmethod


class AbstractBodyWashing(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def wash(self):
        pass


class HandBodyWashing(AbstractBodyWashing):
    def __init__(self):
        super().__init__()
        self.__car_name = "car_name"

    @property
    def get_car_name(self):
        return self.__car_name

    @get_car_name.setter
    def set_car(self, name):
        self.__car_name = name

    def wash(self):
        print(f'Mycie reczne karoserii {self.__car_name}')


class AutomaticBodyWashing(AbstractBodyWashing):
    def __init__(self):
        super().__init__()
        self.__car_name = "car_name"

    @property
    def get_car_name(self):
        return self.__car_name

    @get_car_name.setter
    def set_car(self, name):
        self.__car_name = name

    def wash(self):
        print(f'Mycie automatyczne karoserii {self.__car_name}')


class CreateBodyWashing(AbstractBodyWashing):
    def __init__(self, new_type):
        super().__init__()
        self.__new_type = new_type
        self.__car_name = "car_name"

    @property
    def get_car_name(self):
        return self.__car_name

    @get_car_name.setter
    def set_car(self, name):
        self.__car_name = name

    def wash(self):
        print(f'Opis mycia karoserii: {self.__new_type}\nSamochod: {self.__car_name}')

