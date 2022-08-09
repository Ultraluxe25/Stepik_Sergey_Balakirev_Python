"""
9.3 Функция map (задача 3)
Подвиг 3. Вводится таблица целых чисел. Используя функцию map и генератор списков, преобразуйте список строк lst_in
(см. листинг) в двумерный список с именем lst2D, содержащий целые числа. 

Выводить на экран ничего не нужно, только сформировать список lst2D на основе введенных данных.

Sample Input:
8 11 -5
3 4 10
-1 -2 3
4 5 6

Sample Output:
True
"""

import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список lst_in)
# переменную lst_in не менять!

# print(lst_in)
lst2D = list()
for row in lst_in:
    row = row.split()
    # print(row)
    lst2D.append(list(map(int, row)))
    # print(list(map(int, row)))
