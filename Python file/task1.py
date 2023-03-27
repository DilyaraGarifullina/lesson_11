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
