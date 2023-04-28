#Задание 1
#Создайте класс cat и добавьте 3 атрибута (имя, окрас, возраст) и 3 метода класса (мяукнуть, мурлыкать и еще один на ваше усмотрение).

#Создайте 1 экземпляр класса и продемонстрируйте его атрибуты и методы.
class cat:
    name = ""
    old = ""
    color = ""

    def mya(self):
        print("Мяу, мяу!")

    def makeNoise(self):
        print("*мурчит*")

    def dvig(self):
        print("*перевернулась*")

    def info(self):
        print("Ее зовут", self.name, "и ей", self.old, ". Она", self.color)


obj = cat()
obj.name = 'Мурка'
obj.old = '1 месяц'
obj.color = 'белая'
obj.info()
obj.makeNoise()
obj.mya()
obj.dvig()

#Задание 2
#Создайте класс Good, который будет вычислять значения стоимости товаров. В качестве атрибутов пусть будут:

#name (имя товара),
#price(цена за 1 кг),
#cost (стоимость),
#weight(масса);
#в качестве методов:

#calc - вычисляющий стоимость товара.
#Реализуйте два экземпляра класса Good:

#Яблоки apple('apple', price = 100, weight = 1.5)

#Груши pear('pear', price = 120, weight = 0.8)

#Выведите их стоимость
class Good:
    def __init__(self, name, price, weight):
        self.name=name
        self.price=price
        self.weight=weight
        self.coast=self.calc()
    def calc(self):
        return self.price*self.weight
apple=Good('apple', price = 100, weight = 1.5)
pear=Good('pear', price = 120, weight = 0.8)
print(apple.coast)
print(pear.coast)
#Задание 3
#Создайте класс Car, реализуйте в нем 5 атрибутов :

#цвет,
#марку,
#кузов (сидан sedan, грузовик truck),
#скорость,
#тип коробки передач;
#и 6 методов:

#start - заставляет начинать движение
#stop - останавливает машину
#turn - поворачивает машину в какую-либо сторону, и выводит сообщение:" Машина повернула налево"
#speed_up - ускоряет автомобиль
#speed_down - замедляет автомобиль
#beep - сигналит
#Создайте два экземпляра класса truck и car. Продемонстрируйте работу всех методов

class car:
    def __init__(self, color, brand, body_type, speed, transmission):
        self.color = color
        self.brand = brand
        self.body_type = body_type
        self.speed = speed
        self.transmission = transmission

    def start(self):
        print(f'the {self.color} {self.brand} {self.body_type} starts moving')

    def stop(self):
        print(f'the {self.color} {self.brand} {self.body_type} stop')

    def turn(self, direction):
        print(f'the {self.color} {self.brand} {self.body_type} turns {direction}')

    def speed_up(self, speed):
        self.speed += speed
        print(f'the {self.color} {self.brand} {self.body_type} speeds up to {self.speed} km/h')

    def speed_down(self, speed):
        self.speed += speed
        print(f'the {self.color} {self.brand} {self.body_type} slows down to {self.speed} km/h')

    def beep(self):
        print(f'the {self.color} {self.brand} {self.body_type} beeps')


car_1 = car('red', 'BMW', 'sedan', 95, 'automatic')
truck_1 = car('black', 'Porsche', 'truck', 75, 'manual')

car_1.start()
car_1.speed_up(15)
car_1.turn('left')
car_1.speed_down(10)
car_1.beep()
car_1.stop()

truck_1.start()
truck_1.speed_up(15)
truck_1.turn('left')
truck_1.speed_down(10)
truck_1.beep()
truck_1.stop()
#Задание 4
#Добавьте ограничение скорости в класс Car из предыдущего задания: для грузовика(truck) 60 км/ч, а для легкового(car) - 80 км/ч. При превышении пусть на экран выводится предупреждение: "Скорость превышена! Разрешенная скорость 60 км/ч"

class car:
    def __init__(self, color, brand, body_type, speed, transmission):
        self.color = color
        self.brand = brand
        self.body_type = body_type
        self.speed = speed
        self.transmission = transmission

    def start(self):
        print(f'the {self.color} {self.brand} {self.body_type} starts moving')

    def stop(self):
        print(f'the {self.color} {self.brand} {self.body_type} stop')

    def turn(self, direction):
        print(f'the {self.color} {self.brand} {self.body_type} turns {direction}')

    def speed_up(self, speed):
        if self.body_type == 'truck' and self.speed + speed > 60:
            print('Speed exceeded! The permitted speed is 60 km/h')
        elif self.body_type == 'car' and self.speed + speed > 80:
            print('Speed exceeded! The permitted speed is 80 km/h')
        else:
            self.speed += speed
            print(f'the {self.color} {self.brand} {self.body_type} speeds up to {self.speed} km/h')

    def speed_down(self, speed):
        self.speed += speed
        print(f'the {self.color} {self.brand} {self.body_type} slows down to {self.speed} km/h')

    def beep(self):
        print(f'the {self.color} {self.brand} {self.body_type} beeps')


car_1 = car('red', 'BMW', 'sedan', 95, 'automatic')
truck_1 = car('black', 'Porsche', 'truck', 75, 'manual')

car_1.start()
car_1.speed_up(15)
car_1.turn('left')
car_1.speed_down(10)
car_1.beep()
car_1.stop()

truck_1.start()
truck_1.speed_up(15)
truck_1.turn('left')
truck_1.speed_down(10)
truck_1.beep()
truck_1.stop()
#Задание 5
#Создайте класс светофор (trafficlight). Реализуйте в нем метод, который будет переключать цвета (red, green, yellow) по определенному времени: red = 1 сек, green 2 сек, yellow = 0.5 сек.

#Подсказка:

#Воспользуйтесь модулем time. В нем есть функция sleep
import time
class trafficlight:
    def __init__(self):
        self.color = {'red': 1, 'yellow': 0.5, 'green': 2}

    def running(self):
        for c in self.color:
            print(f'The traffic light switched to: {c}')
            time.sleep(self.color[c])


t = trafficlight()
t.running()