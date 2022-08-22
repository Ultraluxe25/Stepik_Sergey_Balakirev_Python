""" 
7.11 Декораторы функций (Задача 1)
Подвиг 1. Объявите функцию с именем get_sq, которая вычисляет площадь прямоугольника по двум параметрам: width и height - ширина и высота прямоугольника.
И возвращает результат (сама ничего на экран не выводит). То есть, функция имеет сигнатуру:

def get_sq(width, height): ...

Определите декоратор func_show для этой функции, который отображает результат на экране в виде строки (без кавычек):

"Площадь прямоугольника: <значение>"

Вызывать функцию и декоратор не нужно, только объявить. Применять декоратор к функции также не нужно.

Sample Input:
8 11

Sample Output:
Площадь прямоугольника: 88
"""

def get_sq(width, height):
    return width * height


def func_show(function):
    def wrapper(*args, **kwargs):
        print(f"Площадь прямоугольника: {function(*args)}")
        
    return wrapper
