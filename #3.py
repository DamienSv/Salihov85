#3
#Создайте класс Box (посылка), у которого будет приватные атрибуты:
#postcode (номер отправления),
#name (имя отправителя),
#from_city (город отправителя),
#target_city (город назначения).
#Реализуйте методы, которые будут давать возможность доступа к приватным атрибутам.
#Реализуйте метод, который будет давать возможность менять город назанчения
#Назовите модуль task_3_box и сохраните его
class Box:
    def __init__(self, postcode, name, from_city, target_city):
        self.__postcode = postcode
        self.__name = name
        self.__from_city = from_city
        self.__target_city = target_city
    def get_postcode(self):
        return self.__postcode
    def get_name(self):
        return self.__name
    def get_from_city(self):
        return self.__from_city
    def get_target_city(self):
        return self.__target_city
    def set_target_city(self, target_city):
        self.__target_city = target_city
from random import randint
num = randint(100000, 999999)
my_box = Box(num, "Ivan", "London", "Paris")
print("My box postcode:", my_box.get_postcode())
print("My box name:", my_box.get_name())
print("My box from_city:", my_box.get_from_city())
print("My box target_city before change:", my_box.get_target_city())
my_box.set_target_city("Berlin")
print("My box target_city after change:", my_box.get_target_city())