#Задание 1
#Создайте функцию calculate, которая принимает у пользователя два числа и операцию, а выдает результат операции. Обязательно: воспользуйтесь функциями exec или eval
def calc(a,symbol,b):
    return eval(str(a)+symbol+str(b))
#Задание 2
#Пусть дан список имен пользователлей s. Создайте функцию, которая: a) Преобразует имена так, чтобы имена начинались с заглавной буквы. б) Удаляет недопустимые символы (пробелы, цифры и спецсимволы)

#s = ['анТОн', 'НАТАЛЬЯ', 'никита', 'МаРиЯ', '!СЕРГЕЙ!', 'Владимир747', 'Павел+100500']

#Задание 3
#Создайте функцию honest, которая принимает произвольный список, а возвращает список, состоящий только из четных элементов. Список от 0 до 20 создайте любым способом.

#Задание 4
#Создайте функцию cesar, которая возвращает зашифрованную строку шифром Цезаря со сдвигом на 3. Саму строку запросите у пользователя.

#Шифр Цезаря — это вид шифра подстановки, в котором каждый символ в открытом тексте заменяется символом, находящимся на некотором постоянном числе позиций левее или правее него в алфавите. Например, в шифре со сдвигом вправо на 3, А была бы заменена на Г, Б станет Д, и так далее.

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
#Задание 6 *
#Создать функцию alphabet, которая:

#а) выводит буквы английского алфавита и их порядковый номер.

#б) выводит словарь {порядковый номер : буква }

#Задание 7
#Пусть дана функция, которая спрашивает имя пользователя.

#def get_name( ):
#  name = input('Введите имя')
#  return name
#Создайте декоратор hello, который дополнительно будет выводить приветствие: "Привет, <имя>!"

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