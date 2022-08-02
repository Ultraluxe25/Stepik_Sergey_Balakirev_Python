""" 
7.12 Передача аргументов декораторам (Задача 1)
Подвиг 1. Вводится строка целых чисел через пробел. Напишите функцию, которая преобразовывает эту строку в список чисел и возвращает их сумму.

Определите декоратор для этой функции, который имеет один параметр start - начальное значение суммы.
Примените декоратор со значением start=5 к функции и вызовите декорированную функцию для введенной строки s:

s = input()

Результат отобразите на экране.

Sample Input:
5 6 3 6 -4 6 -1

Sample Output:
26
"""

def pre_decorator(start):
    def decorator(function):
        def wrapper(message):
            return function(message) + start 
        return wrapper
    return decorator


@pre_decorator(start=5)
def modificate(text):
    text = [int(i) for i in text.split()]
    return sum(text)


s = input()
result = modificate(s)
print(result)

