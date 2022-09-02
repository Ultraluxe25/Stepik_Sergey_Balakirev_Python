""" 
9.7 Аргумент key для сортировки по ключу (Задача 4)
Значимый подвиг 4. Имеется таблица с данными, представленная в формате:

Номер;Имя;Оценка;Зачет
1;Иванов;3;Да
2;Петров;2;Нет
...
N;Балакирев;4;Да

Эти данные необходимо представить в виде двумерного (вложенного) кортежа. Все числа должны быть представлены как целые числа. Затем, отсортировать данные так,
чтобы столбцы шли в порядке:

Имя;Зачет;Оценка;Номер

Реализовать эту операцию с помощью сортировки. Результат должен быть представлен также в виде двумерного кортежа и присвоен переменной с именем t_sorted.

Программа ничего не должна выводить на экран, только формировать двумерный кортеж с переменной t_sorted.

P. S. Для считывания списка целиком в программе уже записаны начальные строчки.

Sample Input:
Номер;Имя;Оценка;Зачет
1;Портос;5;Да
2;Арамис;3;Да
3;Атос;4;Да
4;д'Артаньян;2;Нет
5;Балакирев;1;Нет

Sample Output:
True
"""

import sys

# считывание списка из входного потока (не меняйте переменную lst_in в программе)
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список строк lst_in)
persons = []

for index, person in enumerate(lst_in):
    number, name, mark, credit = person.split(';')
    if index == 0:  # в первой строке списка lst_in нету чисел
        person_data = (name, credit, mark, number)
    else:  # во всех остальных строках числа срокового типа переводим в целые
        person_data = (name, credit, int(mark), int(number))
    persons.append(person_data)

# print(tuple(persons)) -> (('Имя', 'Зачет', 'Оценка', 'Номер'), ('Портос', 'Да', 5, 1), ('Арамис', 'Да', 3, 2), ('Атос', 'Да', 4, 3),
# ("д'Артаньян", 'Нет', 2, 4), ('Балакирев', 'Нет', 1, 5))   
t_sorted = tuple(persons)  # даже и не знаю зачем усложнять решение, используя сортировку?