""" 
9.8 Функция isinstance для проверки типов данных (Задача 1)
Подвиг 2. Определите функцию с именем get_add, которая складывает или два числа или две строки (но не число со строкой) и возвращает полученный результат.
Если сложение не может быть выполнено, то функция возвращает значение None. Сигнатура функции должна быть, следующей:

def get_add(a, b): ...

Вызывать функцию не нужно, только определить. Также ничего не нужно выводить на экран.

P. S. Не забудьте про необходимость различения булевых значений (False, True) от целочисленных.
"""

def get_add(a, b):
    if type(a) is bool or type(b) is bool:
        return None
    elif type(a) != type(b) and (type(a) is str or type(b) is str):
        return None
    return a + b
