#Задание 1
#Создайте функцию calculate, которая принимает у пользователя два числа и операцию, а выдает результат операции. Обязательно: воспользуйтесь функциями exec или eval
def calc(a,symbol,b):
    return eval(str(a)+symbol+str(b))
#Задание 2
#Пусть дан список имен пользователлей s. Создайте функцию, которая: a) Преобразует имена так, чтобы имена начинались с заглавной буквы. б) Удаляет недопустимые символы (пробелы, цифры и спецсимволы)

#s = ['анТОн', 'НАТАЛЬЯ', 'никита', 'МаРиЯ', '!СЕРГЕЙ!', 'Владимир747', 'Павел+100500']
a)
s = ['анТОн', 'НАТАЛЬЯ', 'никита', 'МаРиЯ', '!СЕРГЕЙ!', 'Владимир747', 'Павел+100500']
s = ('     '.join(s ))
print (s.title())

b)
def clean_names(names):
    cleaned_names = []
    for name in names:
        cleaned_name = ''
        for char in name:
            if char.isalpha():
                cleaned_name += char
        cleaned_names.append(cleaned_name.title())
    return cleaned_names

s = ['анТОн', 'НАТАЛЬЯ', 'никита', 'МаРиЯ', '!СЕРГЕЙ!', 'Владимир747', 'Павел+100500']
cleaned_s = clean_names(s)
print(cleaned_s)
#Задание 4
#Создайте функцию cesar, которая возвращает зашифрованную строку шифром Цезаря со сдвигом на 3. Саму строку запросите у пользователя.
#Шифр Цезаря — это вид шифра подстановки, в котором каждый символ в открытом тексте заменяется символом, находящимся на некотором постоянном числе позиций левее или правее него в алфавите. Например, в шифре со сдвигом вправо на 3, А была бы заменена на Г, Б станет Д, и так далее.
def a(lst):
    return [x for x in lst if x % 2 == 0]
lst = list(range(21))
res = a(lst)
print(res)

#Задание 5
#Создайте функцию countdown, которая принимает список рандомных чисел от 0 до 10, а возвращает каждый элемент этого списка в порядке обратного отсчета, а после 0 - слово " Пуск!".
#Например:
#countdown(s)
#3 2 1 0 Пуск!
#Можете создать список сами или воспользоваться S=[0,7, 5, 9, 3, 8, 6, 2, 1].
#Для тех, кому интересно:
#для создания рандомного числа, можно воспользоваться функцией sample из модуля random
#[ ]
#from random import sample
#print(sample(range(0, 10), 10))
#[4, 7, 2, 5, 9, 1, 6, 8, 3, 0]
def countdown(S):
    S.sort(reverse = True)
    for i in range(len(S)):
        print(S[i])
    print("Пуск!")
S = [0, 7, 5, 9, 3, 8, 6, 2, 1]
countdown(S)

#Задание 6 *
#Создать функцию alphabet, которая:

#а) выводит буквы английского алфавита и их порядковый номер.

#б) выводит словарь {порядковый номер : буква }
# a)
alp = []
def alphabet(alp):
    for i in range(97, 123):
        print(f"{chr(i)}: {i-96}")
alphabet(alp)

# b)
def alphabet():
    d = {}
    for i in range(26):
        d[i+1] = chr(i+97)
    return d
print(alphabet())

#Задание 7
#Пусть дана функция, которая спрашивает имя пользователя.

#def get_name( ):
#  name = input('Введите имя')
#  return name
#Создайте декоратор hello, который дополнительно будет выводить приветствие: "Привет, <имя>!"
def hi(func):
    def wrapper():
        name = func()
        print(f"Привет, {name}!")
    return wrapper

@hi
def name():
    print("Введите имя:")
    name = input()
    return name

name()

#Задание 8 *
#Предположим, что объявлена функция, которая подставляет в шаблон значения переменной field:

#def render_input(field):
#  return f'<input id="id_{field}" name="{field}">'

#username = render_input('username')
#print(username)
#Создайте декоратор, который обернет строку в теги

#<p> ... </p>
#Пример вывода:

#<p><input id="id_username" name="username"></p>
def name(func):
    def wrapper(*args, **kwargs):
        return f'<p>{func(*args, **kwargs)}</p>'

    return wrapper
@name
def render_input(field):
    return f'<input id="id_{field}" name="{field}">'
username = render_input('username')
print(username)