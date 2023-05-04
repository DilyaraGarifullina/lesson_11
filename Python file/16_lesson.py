#Задание 1
#Создайте родительский класс Animal, у которого есть 3 атрибута:
#color - цвет
#name - кличка
#age - возраст
#и абстрактный метод:
#say - издать звук.
#Создайте два класса потомка - Cat и Dog, в которых будет переопределен метод say: для класса Cat - Meow!, для Dog - Woof!
from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, color, name, age):
        self.color = color
        self.name = name
        self.age = age
        @abstractmethod
        def say(self):
            pass
class Cat(Animal):
    def say(self):
        return 'Meow!'

class Dog(Animal):
    def say(self):
        return 'Woof!'

cat = Cat('orange', 'Murka', 1)
dog = Dog('black', 'Wolff', 6)


print(f'{cat.name} ({cat.color}, {cat.age} year(s) old) says {cat.say()}')
print(f'{dog.name} ({dog.color}, {dog.age} year(s) old) says {dog.say()}')

#Задание 2
#Создайте базовый класса Father, у которого есть два атрибута: name (имя) и surname (фамилия); и дочерний класс Child, у которого будут унаследованы те же атрибуты и дополнительно атрибут patronim (отчество). Создайте один экземпляр класса Child.
class Father:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

class Child(Father):
    def __init__(self, name, surname, patronim):
        super().__init__(name, surname)
        self.patronim = patronim

child = Child("Диляра", " Гарифуллина","Ильясовна")
print(child.name, child.surname, child.patronim)

#Задание 3
#А) Реализовать класс Stationery (канцелярия):

#определить в нём атрибут title (название) и абстрактный метод draw (отрисовка);
#создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
#в классу Pen добавьте атрибут color = 'blue';
#в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение, например: "Ручка пишет";
#создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
#Б)

#Добавьте в класс Stationary метод класса set_color, который присваивает атрибут класса Stationary color;
#Вызовете метод set_color и установите color='yellow';
#Вызовете атрибуты color у классов Pen, Pencil, Handle. Что вы наблюдаете?
from abc import ABC, abstractmethod


class Stationery(ABC):
    def __init__(self, title):
        self.title = title

    @abstractmethod
    def set_color(self, color):
        self.color = color

    @abstractmethod
    def draw(self):
        pass


class Pen(Stationery):
    color = 'blue'

    def draw(self):
        print("Ручка пишет")


class Pencil(Stationery):
    def draw(self):
        print("Карандаш чертит")


class Handle(Stationery):
    def draw(self):
        print("Маркер рисует")


pen = Pen("Ручка")
pencil = Pencil("Карандаш")
handle = Handle("Маркер")

pen.draw()
pencil.draw()
handle.draw()

Stationery.self_color('yellow')
print(Pen.color)
print(Pencil.color)
print(Handle.color)
#Задание 4
#Создайте базовый класс User с атрибутами login, password и методом:
#view - выводит сообщение "Я - User. Могу просматривать содержимое"
#Создайте дочерний класс Moderator, у которого так же будут атрибуты login и password и дополнительно - group_id, а так же два метода:
#view - выводит сообщение "Я - Moderator. Могу просматривать содержимое"
#redact - выводит сообщение "Я - Moderator. Могу редактировать содержимое"

class User:
    def __init__(self, login, password):
        self.login = login
        self.password = password

    def view(self):
        print("Я - User. Могу просматривать содержимое")


class Moderator(User):
    def __init__(self, login, password, group_id):
        super().__init__(login, password)
        self.group_id = group_id

    def view(self):
        print("Я - Moderator. Могу просматривать содержимое")

    def redact(self):
        print("Я - Moderator. Могу редактировать содержимое")


user = User("user_login", "user_password")
moderator = Moderator("8541851", "54154", "911")

user.view()
moderator.view()
moderator.redact()
#Задание 5
#Создайте класс Clock со статичным методом Say_time, который будет выводить на экран текущее время.

#Подсказка: для этого можете воспользоваться стандартной библиотекой time.

#[ ]
#from time import time, localtime

# time выводит количество секунд, прошедших с 1 января 1970, 00:00:00

#print(time()) # 1668680736.59019

# localtime преобразует секунды в кортеж struct_time

#print(localtime(time())) # time.struct_time(tm_year=2022, tm_mon=11, tm_mday=17, tm_hour=10, tm_min=26, tm_sec=8, tm_wday=3, tm_yday=321, tm_isdst=0)

# Чтобы привести его в красивый вид, можно воспользоваться f-строкой

#rez = localtime(time())
#print(f'{rez.tm_hour}:{rez.tm_min}:{rez.tm_sec}') # 10:29:45
#1668680985.4531398
#10:29:45
from time import time, localtime
class Clock:
    @staticmethod
    def Say_time():
        time = localtime()
        print(f'Текущее время: {time.tm_hour}:{time.tm_min}:{time.tm_sec}')

Clock.Say_time()