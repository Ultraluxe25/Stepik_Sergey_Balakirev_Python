""" 
10.2 Битовые операции И, ИЛИ, НЕ, XOR (Задача 6)
Подвиг 9. На вход программы подается целое десятичное число. Используя битовые операции, проверьте, включен ли 5-й или 1-й биты введенного числа. 
Если включен хотя бы один из этих битов, то выведите слово ДА, иначе - слово НЕТ.

Sample Input:
74

Sample Output:
ДА
"""

mask_1 = 0b00100000
mask_2 = 0b00000010
number = int(input())
print('ДА' if mask_1 == number & mask_1 or mask_2 == number & mask_2 else 'НЕТ')

