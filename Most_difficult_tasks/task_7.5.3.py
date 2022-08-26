""" 
7.5 Функции с произвольным числом параметров (Задача 3)
Значимый подвиг 7. (Для закрепления предыдущего материала).
Объявите функцию с именем str_min, которая сравнивает две переданные строки и возвращает минимальную из них (то есть,
выполняется лексикографическое сравнение строк). Затем, используя функциональный подход к программированию (то есть,
более сложные функции реализуются путем вызова более простых), реализовать еще две аналогичные функции:

- с именем str_min3 для поиска минимальной строки из трех переданных строк;
- с именем str_min4 для поиска минимальной строки из четырех переданных строк.

Выполнять функции не нужно, только записать.
"""

def str_min(s1, s2):
    return min(s1, s2)


def str_min3(s1, s2, s3):
    return min(str_min(s1, s2), s3)


def str_min4(s1, s2, s3, s4):
    return min(str_min3(s1, s2, s3), s4)
