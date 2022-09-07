""" 
10.3 Модуль random стандартной библиотеки (Задача 2)
Подвиг 5. Вводится таблица целых чисел, записанных через пробел.
Необходимо перемешать столбцы этой таблицы, используя функции shuffle и zip и вывести результат на экран (также в виде таблицы).

P. S. Для считывания списка целиком в программе уже записаны начальные строчки.

Sample Input:
1 2 3 4
5 6 7 8
9 8 6 7

Sample Output:
4 1 3 2
8 5 7 6
7 9 6 8
"""

"""Нужно поменять  местами только столбцы, поэтому после того как список строк мы превратим во вложенные списки чисел (рядов матрицы)
нужно её транспонировать с помощью zip(). Затем столбцы станут строками и мы сможем их random.shuffle() перетасовать.
Затем мы просто вернём исходную размерность матрицы, транспонировав её снова с помощью zip()."""

import sys
import random
# установка "зерна" датчика случайных чисел, чтобы получались одни и те же случайные величины
random.seed(1)

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу
# print(lst_in) -> ['1 2 3 4', '5 6 7 8', '9 8 6 7']

table = list(map(lambda x: list(map(int, x.split())), lst_in))
# print(table) -> [[1, 2, 3, 4], [5, 6, 7, 8], [9, 8, 6, 7]]

zip_table = list(zip(*table))  # '*' for work with 3 lists
# print(zip_table) -> [(1, 5, 9), (2, 6, 8), (3, 7, 6), (4, 8, 7)]

# print(random.shuffle(zip_table)) -> None. That's why we just call but not print this function
random.shuffle(zip_table)  # we shuffle our table's rows

# we have to zip our table (transponate) because we need to shuffle just colomns
# and return original matrix sizes
shuffle_table = list(zip(*zip_table))  # return to our first view of the table
for row in shuffle_table:  #  output each row
    print(*row)
