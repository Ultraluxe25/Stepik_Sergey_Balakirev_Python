""" 
4.2 Вложенные условия и множественный выбор (Задача 1)
Подвиг 6. Дата некоторого дня характеризуется двумя натуральными числами: m (порядковый номер месяца) и n (число).
По введенным m и n (в одну строку через пробел) определить:

а) дату предыдущего дня (принять, что m и n не характеризуют 1 января);
б) дату следующего дня (принять, что m и n не характеризуют 31 декабря).

В задаче принять, что год не является високосным.
Вывести предыдущую дату и следующую дату (в формате: mm.dd, где m - число месяца; d - номер дня) в одну строчку через пробел.

P.S. Число дней в месяцах не високосного года, начиная с января: 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31

Sample Input:
8 31

Sample Output:
08.30 09.01
"""

import datetime
month, day = map(int, input().split())

today = datetime.datetime(2021, month, day)

yesterday = today - datetime.timedelta(days=1)
tomorrow = today + datetime.timedelta(days=1)

yesterday = str(yesterday)[5:10]
tomorrow = str(tomorrow)[5:10]

yesterday = yesterday.replace('-', '.')
tomorrow = tomorrow.replace('-', '.')

print(yesterday, tomorrow)
