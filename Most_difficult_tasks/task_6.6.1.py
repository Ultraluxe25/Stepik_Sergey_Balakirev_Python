""" 
6.6 Генераторы множеств и словарей (Задача 1)
Подвиг 2. Вводится строка со списком оценок, например:

2 неудовлетворительно удовлетворительно хорошо отлично

Первая цифра - это числовое значение первой оценки. Остальные оценки имеют возрастающие на 1 числа.
С помощью генератора словарей необходимо сформировать словарь d, где ключами будут выступать числа, а значениями - слова.
Например:

d = {2: 'неудовлетворительно', 3: 'удовлетворительно', 4: 'хорошо', 5: 'отлично'}

Вывести на экран значение сформированного словаря с ключом 4.

Sample Input:
1 ужасно неудовлетворительно удовлетворительно прилично отлично

Sample Output:
прилично
"""

marks = input().split()
assessment = marks[1:]
lowest_mark = int(marks[0])

marks = {mark for mark in range(lowest_mark, lowest_mark + len(assessment))}
# print(marks)
description = [element for element in assessment]
# print(description)
student_book = dict()
for index, value in enumerate(marks):
    student_book[value] = description[index]
# print(student_book)
print(student_book[4])
