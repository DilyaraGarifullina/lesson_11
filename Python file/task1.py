#Гарифуллина Диляра 911 группа
#Задание 1
#Создайте функцию calculator, которая принимает у пользователя два числа и операцию(+, -, /, *), а возвращает
#результат. Предусмотрите предупреждение об ошибке при делении на 0.
a, b = int(input()), int(input())
operetion = input()
if operetion == '+':
    print(a + b)
elif operetion == '-':
    print(a - b)
elif operetion == '*':
    print(a * b)
elif operetion == '/' and b != 0:
    print(a / b)
elif b == 0 and operetion == '/':
    print('На ноль делить нельзя')
else:
    print('Неверная операция')

#Задание 2
#Создайте функцию reverse, которая принимает неограниченное число слов, а возвращает слово с развернутыми буквами. Например:
#reverse('Привет')
#"тевирП"
#Пользоваться срезами в данном задании запрещено

n = input()
print(''.join(reversed(f'{n}')))

#Задание 3
#Создайте функцию hello, которая запрашивает имя у пользователя. Если такое мя есть в списке - выдает : "Привет,
#<имя>!", если нет - то добавляет его в список и выдает : "Привет, <имя>! Рад знакомству!".
#Протестируйте ее на нескольких примерах

def hello ():
  n=[ ]
  while True:
    name = input('Как вас зовут?')
    if name in n:
      print(f'Привет, {name},!')
    else:
      print(f'Привет, {name},! Рад знакомству!')
      n.appenend(name)
hello ()

#Задание 4
#Создайте функцию count, которая выводит числа от 0 до 10. Решите эту задачу с помощью: а) цикла while б) с помощью рекурсии
#a
def count():
  i = 0
  while i <= 10:
    print(i)
    i += 1
count()

#b
def count(i = 0):
  print(i)
  if i>=10:
    return
  count(i+1)
count()

#Задание 4 *
#Создайте функцию count, которая выводит количество четных и нечетных чисел от 0 до 10. Решите эту задачу с помощью:
#а) цикла while б) с помощью рекурсии

#a
def count():
  odd = 0
  mean = 0
  n = int(input())
  i = 1
  while i <= n:
    if i % 2 ==0:
      odd +=1
    else:
      mean += 1
    i += 1
  print(f'четные{odd}, нечетные {mean}')
count()

#b
def count(odd = 0, mean = 0, n = int(input()), i = 1):
  while i <= n:
    if i % 2 == 0:
      odd += 1
    else:
      mean += 1
    count(odd, mean, n, i+1)
  return (f'четные{odd}, нечетные {mean}')
print(count())

#Задание 5 *
#Создайте функцию Fibonacci, которая генерирует список чисел Фибоначчи меньше 100.
#а) решите эту задачу с помощью цикла while
#б) решите эту задачу с помощью рекурсии
#Ряд Фибоначчи:первые два числа 0 и 1, а потом каждое последующее число = сумма двух предыдущих.
#например:0 1 1 2 3 5 8 13 21 и т.д.
#0 + 1 = 1
#1 + 2 = 3
#3 + 5 = 8
#5 + 8 = 13
#a
def fibonacci (i=0, j=1, lst=[0]):
  while i<100:
    print(lst)
    lst.append(j)
    i, j=j, i+j
fibonacci()
#b
def fibonacci (i=0, j=1, lst=[0]):
  print(lst)
  if j<100:
    lst.append(j)
    i, j=j, i+j
    fibonacci(i, j, lst)
  else:
    return lst
fibonacci()

#Задание 6 *
#Создайте функцию factorial, которая принимает число и вычисляет факториал этого числа.
#Факториал 5: 5! = 1 * 2 * 3 * 4 * 5 а) решите эту задачу с помощью цикла while б) решите эту задачу с помощью рекурсии
#a
def factorial ():
  n = int(input())
  rez = 1
  if n < 1:
    return rez
  rez *= n
  return factorial(n-1, rez)
print(factorial())
#b
def factorial (n = int(input()), rez = 1):
  if n < 1:
    return rez
  rez *= n
  return factorial(n-1, rez)
print(factorial())

#Задание 7 *
#Создайте функцию login, которая запрашивает у пользователя логин и пароль, проверяет его по базе и:
#если логин, пароль совпадают - выдает "Доступ разрешен", если логин и пароль не совпадают - "Доступ запрещен",
#а если пользователя с таким логином нет, записывает его в базу и выдает : "Регистрация прошла успешно".
#Базу можно реализовать с помощью одного из встроенных типов данных в Python. Как вы думаете, какой подойдет?

def login(log, pas):
  pas =dct.get(log)
  if pas == pas:
    print("доступ разрешен")
  else:
    print("доступ запрещен")
  if log not in dct:
    ans=input("Вы хотите зарегистрироваться? Да\Нет")
    if ans ==("да"):
      dct[log]=pas
      print("вы зарегистрированы")
    else:
      print("вы не зарегистрированы")
dct={ }
while True:
  login(log=("логин"), pas = input("пароль:"))

#Задание 8 **
#В программе генерируется случайное целое число от 0 до 100. Пользователь должен его отгадать не более чем за 10 попыток.
#После каждой неудачной попытки должно сообщаться больше или меньше введенное пользователем число, чем то, что загадано.
#Если за 10 попыток число не отгадано, то вывести загаданное число.
#Решите через рекурсию. В задании нельзя применять циклы.
#Случайное число можно сгенерировать с помощью функци randint модуль random:
#from random import randint
#randint(start,stop)

from random import randint
n = randint (0, 100)
print (n)
def number (m):
  att= 1
  if m==n:
    print ("Yes! You guessed it!")
  else:
    while att != 10:
      if m>n:
        m = int (input ("Enter a number less "))
      elif m<n:
        m = int(input("Enter a number greater "))
      att += 1
      if m==n:
        print("Yes! You guessed it!")
        return n
    else:
      print ("I'm sorry, but you lost. It was" + str(n))
      return n

number(m=int(input("Enter a number")))