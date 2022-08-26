""" 
5.6 Вложенные циклы (Задача 1)
Подвиг 2. Вводится список из URL-адресов (каждый с новой строки). Требуется в них заменить все пробелы на символ дефиса (-).
Следует учесть, что может быть несколько подряд идущих пробелов. Результат преобразования вывести на экран в виде строк из URL-адресов.

P. S. Для считывания списка целиком в программе уже записаны начальные строчки.

Sample Input:
django chto  eto takoe    poryadok ustanovki
model mtv   marshrutizaciya funkcii  predstavleniya
marshrutizaciya  obrabotka isklyucheniy       zaprosov perenapravleniya

Sample Output:
django-chto-eto-takoe-poryadok-ustanovki
model-mtv-marshrutizaciya-funkcii-predstavleniya
marshrutizaciya-obrabotka-isklyucheniy-zaprosov-perenapravleniya
"""

import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список lst_in)
for i in lst_in:
    i = i.replace(' ', '-')
    while '--' in i:
        i = i.replace('--', '-')
    print(i)
