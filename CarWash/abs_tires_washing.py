from abc import ABC, abstractmethod


class AbstractTiresWashing(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def wash(self):
        pass


class HandTiresWashing(AbstractTiresWashing):
    def __init__(self):
        super().__init__()
        self.__car_name = " "

    @property
    def get_car_name(self):
        return self.__car_name

    @get_car_name.setter
    def set_car(self, name):
        self.__car_name = name

    def wash(self):
        print(f'Mycie reczne opon {self.__car_name}')


class AutomaticTiresWashing(AbstractTiresWashing):
    def __init__(self):
        super().__init__()
        self.__car_name = " "

    @property
    def get_car_name(self):
        return self.__car_name

    @get_car_name.setter
    def set_car(self, name):
        self.__car_name = name

    def wash(self):
        print(f'Mycie automatyczne opon {self.__car_name}')


class CreateTiresWashing(AbstractTiresWashing):
    def __init__(self, new_type):
        super().__init__()
        self.__new_type = new_type
        self.__car_name = " "

    @property
    def get_car_name(self):
        return self.__car_name

    @get_car_name.setter
    def set_car(self, name):
        self.__car_name = name

    def wash(self):
        print(f'Opis mycia opon: {self.__new_type}\nSamochod: {self.__car_name}')
