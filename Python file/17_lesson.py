#Задание 1
#Представьте себе стопку книг. Вы кладете первую, на нее вторую и т.д. А теперь хотите убрать книги. Если вы уберете нижнюю - то вся стопка развалится. Поэтому нужно убирать сверху. В этом и заключается тип данных Stack - куча или стопка.
#Такой способ организации данных получил название LIFO (англ. last in, first out «последним пришёл — первым ушёл»).
#Задание: Создайте класс Batary, у которой будет определен атрибут capacity = [ ] (емкость), max_charge = 5 (максимальный заряд) по умолчанию, и методы:
#charge - заряжает батарею
#discharge - разряжает батарею.
#Переопределите метод __str__, чтобы при вызове экземпляра он представлялся в виде: [)))))] - максимально заряженная батарея.
#Подсказка: можете использовать методы очень похожего стандартного типа данных. Догадались какого?

class Batary:
    def __init__(self, max_charge=5):
        self.capacity = []
        self.max_charge = max_charge

    def charge(self):
        if len(self.capacity) < self.max_charge:
            self.capacity.append(")")
        else:
            print("Аккумулятор полностью заряжен")

    def discharge(self):
        if len(self.capacity) > 0:
            self.capacity.pop()
        else:
            print("Батарея разряжена")

    def __str__(self):
        return "[" + "".join(self.capacity) + "]"


b = Batary()
print(b)

b.charge()
print(b)

b.charge()
print(b)

b.charge()
print(b)

b.charge()
print(b)

b.discharge()
print(b)

b.discharge()
print(b)

b.discharge()
#Задание 2
#Представьте себе очередь на кассе. К кассе подходит первый человек в очереди, а в конец очереди встает вновь пришедший. В программировании есть подобный тип данных - Queue (англ. "очередь"), основанный на принципе FIFO (англ. first in, first out «первым пришёл — первым ушёл»).

#Задание:
#Реализовать класс Queue
#Определить атрибут inside, который будет хранить в себе имена людей в очереди.
#Переопределить метод __str__, чтобы преобразовать его к виду: Name1=>Name2=>...=>Name3
#Реализовать методы:
#add - который добавляет имя в очередь
#take_out убирает первого человека из списка
#Переопределить методы __add__ , __sub__, __iadd__, __isub__ чтобы они соответствовали методам add и take_out

class Queue:
    def __init__(self):
        self.inside = []

    def __str__(self):
        return ' => '.join(self.inside)

    def add(self, name):
        self.inside.append(name)

    def take_out(self):
        if self.inside:
            return self.inside.pop(0)
        else:
            return 'Нет очереди'

    def __iadd__(self, name):
        self.add(name)
        return self

    def _isub_(self, name):
        self.take_out()
        return self

    def _add_(self, name):
        new_queue = Queue()
        new_queue.inside = self.inside.copy()
        new_queue.add(name)
        return self

    def __sub__(self, name):
        new_queue = Queue()
        new_queue.inside = self.inside.copy()
        new_queue.take_out()
        return new_queue


queue = Queue()

queue.add("Миша")
queue.add("Катя")
queue.add("Котик")
print(queue)

queue.take_out()
print(queue)

queue += "Миша"
print(queue)

queue += "Катя"
print(queue)

queue -= "Котик”
print(queue)


#Задание 3
#a) Создайте класс Matrix
#который должен принимать данные (список списков) для формирования матрицы.
#Пример ввода:
#m1 = Matrix([[1,2,3], [4,5,6]])
#это мы ввели матрицу:

#1 2 3
#4 5 6
#Подсказка
#Матрица - система некоторых математческих величин, расположенных в виде прямоугольной схемы.

#примеры матриц:

#0  0        7  8  9
#0  0        10 3 -1
            12 3  4
#b) Следующий шаг
#реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.

#c) Далеее
#реализовать перегрузку метода __add__() для сложения двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.

#Пример:
#m1 = Matrix([[1,2,3],[4,5,6]])
#m2 = Matrix([[6,5,4],[3,2,1]])
#m3 = m1 + m2
#print(m3)

#7 7 7
#7 7 7
#Подсказка
#При сложении матриц одинакового размера складываются элементы на тех же местах из двух разных матриц:

#1 2 3  +  6 5 4  = 7 7 7
#4 5 6     3 2 1    7 7 7

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0])

    def __str__(self):
        result = ''
        for i in range(self.rows):
            for j in range(self.cols):
                result += str(self.matrix[i][j]) + ''
            result += '\n'
        return result

    def __add__(self, other):
        result = [[0 for j in range(self.cols)] for i in range(self.rows)]
        for i in range(self.rows):
            for j in range(self.cols):
                result[i][j] = self.matrix[i][j] + other.matrix[i][j]
        return Matrix(result)


m1 = Matrix([[21, 5], [7, 4]])
m2 = Matrix([[0, 3], [6, 10]])
m3 = m1 + m2
print(m3)