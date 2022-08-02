"""
9.1 Выражения-генераторы (задача 5)

Подвиг 7. Используя символы малых букв латинского алфавита (строка ascii_lowercase):
from string import ascii_lowercase

запишите генератор, который бы возвращал все сочетания из двух букв латинского алфавита. Выведите первые 50 сочетаний на экран в строку через пробел.

Например, первые семь начальных сочетаний имеют вид:
aa ab ac ad ae af ag
"""

from string import ascii_lowercase  # ascii_lowercase == 'abcdefghijklmnopqrstuvwxyz'

# generator = (i + j for i in ascii_lowercase for j in ascii_lowercase)
counter = 0
while counter < 50:    
    for i in ascii_lowercase:
        if counter >= 50:
            break
            
        generator = (j for j in ascii_lowercase)
        for j in generator:
            if counter >= 50:
                break
                
            print(i + j, end=" ")
            counter += 1
