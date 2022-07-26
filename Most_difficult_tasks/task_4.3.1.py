""" 
4.3 Тернарный условный оператор (Задача 1)
Подвиг 6. Имеется список базовых нот:

m = ['до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си']

Вводятся три целых числа в диапазоне от 1 до 7 - номера нот, в одну строчку через пробел.
Необходимо отобразить указанные ноты в виде строки через пробел, но перед нотами до и фа дополнительно ставить символ диеза '#'.
Реализовать эту программу с использованием тернарного условного оператора (он может использоваться несколько раз).

Sample Input:
1 6 7

Sample Output:
#до ля си
"""

m = ['до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си']
a, b, c = map(int, input().split())

m1 = m[a - 1]
m2 = m[b - 1]
m3 = m[c - 1]

m1 = '#' + m1 if m1 == m[0] or m1 == m[3] else m1
m2 = '#' + m2 if m2 == m[0] or m2 == m[3] else m2
m3 = '#' + m3 if m3 == m[0] or m3 == m[3] else m3

print(m1, m2, m3)
