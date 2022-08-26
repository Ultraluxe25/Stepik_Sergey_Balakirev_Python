""" 
7.5 Функции с произвольным числом параметров (Задача 1)
Подвиг 5. Объявите функцию с именем get_data_fig для вычисления периметра произвольного N-угольника.
На вход этой функции передаются N длин сторон через аргументы. Дополнительно могут быть указаны именованные аргументы:

type - булево значение True/False
color - целое числовое значение
closed - булево значение True/False
width - целое значение

Функция должна возвращать в виде кортежа периметр многоугольника и указанные значения именованных параметров в порядке их перечисления в тексте задания
(если они были переданы). Если какой-либо параметр отсутствует, его возвращать не нужно (пропустить).

Функцию выполнять не нужно, только определить.
"""

def get_data_fig(*sides, **kwargs):
    perimeter = 0
    for side in sides:
        perimeter += side
    result = (perimeter, )
    
    if 'type' in kwargs.keys():
        result += (kwargs['type'], )
    if 'color' in kwargs.keys():
        result += (kwargs['color'], )
    if 'closed' in kwargs.keys():
        result += (kwargs['closed'], )
    if 'width' in kwargs.keys():
        result += (kwargs['width'], )
        
    return result
