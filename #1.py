#1 
#Сооздайте класс Person с приватными атрибутами name, age, surname. Реализуйте методы name, 
#age, surname, которые будут давать доступ к аналогичным приватным атрибутам. Создайте сеттер, который будет давать возможность поменять атрибут age.
class Person:
    def __init__(self, name, age, surname):
        self.__name = name
        self.__age = age
        self.__surname = surname

    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age
    def get_surname(self):
        return self.__surname
    def set_age(self, age):
        self.__age = age

person = Person("Лёша", 25, "Иванов")
print("Имя:", person.get_name())
print("Возраст:", person.get_age())
print("Фамилия:", person.get_surname())
person.set_age(30)
print("Имя:", person.get_name())
print("Возраст:", person.get_age())
print("Фамилия:", person.get_surname())