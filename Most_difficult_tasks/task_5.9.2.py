""" 
5.9 Вложенные циклы и вложенные генераторы списков (Задача 2)
Подвиг 2. Вводится список целых чисел в строку через пробел.
С помощью list comprehension сформировать из них двумерный список lst размером N x N (квадратную таблицу чисел).
Гарантируется, что из набора введенных чисел можно сформировать квадратную матрицу (таблицу). Результат отобразить в виде списка командой:

print(lst)
 
Sample Input:
1 2 3 4 5 6 7 8 9

Sample Output:
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
"""

num = [int(i) for i in input().split()]
n = int(len(num) ** 0.5)  # устанавливаем размерность кв. матрицы
counter = 0
a = []  # создаём счётчик и новый внешний список

while counter < len(num):  # счётчик в роли итератора
    b = []
    for i in range(n):
        b.append(num[counter])  # наполняем вложенный список
        counter += 1  # тоже что и next()
    a.append(b)  # добавляем вложенный список во внешний

print(a)
