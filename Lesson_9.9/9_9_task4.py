""" 
9.9 Функции all и any (Задача 4)
Подвиг 4. Вводятся оценки студента в одну строчку через пробел. Необходимо определить, имеется ли в этом списке хотя бы одна оценка ниже тройки.
Если это так, то вывести на экран строку "отчислен", иначе - "учится".

Задачу реализовать с использованием одной из функций: any или all.

Sample Input:
3 3 3 2 3 3

Sample Output:
отчислен
"""

def check_marks(marks):
    return 'отчислен' if any(map(lambda x: x < 3, marks)) else 'учится'


numbers = [int(i) for i in input().split()]
# print(numbers)
print(check_marks(numbers))
