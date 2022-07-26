""" 
10.2 Битовые операции И, ИЛИ, НЕ, XOR (Задача 2)
Подвиг 3. На вход программы подается целое десятичное число. Используя битовые операции, выключите 4-й и 1-й биты введенного числа.
Выведите на экран полученное числовое значение.

Sample Input:
153

Sample Output:
137
"""

number = int(input())
mask = 0b11101101  # устанавливаем число в котором все биты включены,
# кроме тех, которые нужно выключить у некоторого числа
print(number & mask)
