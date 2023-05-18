#4
#Реализуйте класс Truck (грузовик). Грузовик может перевозить посылки - Box из предыдущего задания
#Импортиуйте модуль task_3_box из предыдущего задания.
#Создайте несколько экземпляров класса Box.
#Проверьте работу методов класса Box
#Создайте класс Truck (грузовик), который будет иметь несколько атрибутов, присущих грузовику.
#Реализуйте атрибут capacity (емкость), в котором будет реализовано хранилище посылок (Box): [box1, box2 ...]
#Переопределите методы __str__, __add__, __sub__ для реализации отображения грузовика, загрузки и выгрузки посылок.
#Продемонстрируйте работу класса Truck.
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

class Truck:
  def __init__(self, capacity):
    self.capacity = capacity
  def __str__(self):
    return f"Truck with capacity of {len(self.capacity)} boxes: {', '.join(map(str, self.capacity))}"
  def __add__(self, box):
    self.capacity.append(box)
    return self
  def __sub__(self, box):
    self.capacity.remove(box)
    return self

box1 = Box('11111', 'Ivan', 'Moscow', 'St. Petersburg')
box2 = Box('22222', 'Petr', 'Novosibirsk', 'Irkutsk')
print(box1.get_postcode()) 
print(box2.get_name()) 
box2.set_target_city('Krasnoyarsk')
print(box2.get_target_city()) 
truck = Truck([])
truck += box1
print(truck) 
truck -= box1
print(truck) 

print(truck)  
print(truck - box1)  
print(truck)  