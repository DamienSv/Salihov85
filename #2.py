#2 
#Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта - одежда (Cloth), которая может иметь определенное название. 
#К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто Coat) и рост (для костюма Suit). Это могут быть обычные числа V и H соответственно.
#Для определения расхода ткани по каждому типу одежды использовать формулы:
#для пальто V/6.5+0.5
#для костюма 2H+0.3 Проверить работу этих методов на реальных данных.
#Выполнить общий подсчет расхода ткани, который пойдет на пошив всех костюмов и всех пальто соответственно. Реализовать абстрактыне классы для основных классов проекта и проверить работу декоратора @property.

#Подсказка:
#Воспользуйтесь абстрактным классом при создании класса Cloth
#Определите абстрактные методы подсчета количества ткани
#Количество ткани reserved сделайте атрибутом класса ( определяется вне конструктора)
from abc import ABC, abstractmethod

class Cloth(ABC):
    reserved = 0
    
    @abstractmethod
    def calculate_fabric(self):
        pass

class Coat(Cloth):
    
    def __init__(self, size):
        self.size = size
    
    def calculate_fabric(self):
        return self.size/6.5 + 0.5
    
    @property
    def total_fabric(self):
        return self.reserved + self.calculate_fabric()

class Suit(Cloth):
    
    def __init__(self, height):
        self.height = height
    
    def calculate_fabric(self):
        return 2*self.height + 0.3
    
    @property
    def total_fabric(self):
        return self.reserved + self.calculate_fabric()
coat1 = Coat(50)
coat2 = Coat(60)

suit1 = Suit(170)
suit2 = Suit(180)

Coat.reserved = 0.5*2 
Suit.reserved = 2.3*2 


total_coats = 2
total_suits = 2

total_fabric_coats = total_coats*Coat.reserved
total_fabric_suits = total_suits*Suit.reserved

fabric_coat1 = coat1.total_fabric
fabric_coat2 = coat2.total_fabric
fabric_suit1 = suit1.total_fabric
fabric_suit2 = suit2.total_fabric

print(f"Расход ткани на {total_coats} пальто: {total_fabric_coats} метров")
print(f"Расход ткани на {total_suits} костюма: {total_fabric_suits} метров")
print(f"Расход ткани на пальто размера {coat1.size}: {fabric_coat1} метров")
print(f"Расход ткани на пальто размера {coat2.size}: {fabric_coat2} метров")
print(f"Расход ткани на костюм высотой {suit1.height}: {fabric_suit1} метров")
print(f"Расход ткани на костюм высотой {suit2.height}: {fabric_suit2} метров")