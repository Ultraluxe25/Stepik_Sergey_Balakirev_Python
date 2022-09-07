""" 
9.9 Функции all и any (Задача 1)
Подвиг 1. Вводится строка целых чисел через пробел. Необходимо определить, являются ли все эти числа четными.
Вывести True, если это так и False - в противном случае.

Задачу реализовать с использованием одной из функций: any или all.

Sample Input:
2 4 6 8 22 56

Sample Output:
True
"""

def is_even(collection):
    return all(map(lambda x: x % 2 == 0, collection))


numbers = [int(i) for i in input().split()]
# print(numbers)
print(is_even(numbers))
