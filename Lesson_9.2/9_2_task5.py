"""
9.2 Функция-генератор. Оператор yield (задача 5)
Подвиг 5. Определите функцию-генератор, которая бы возвращала простые числа. (Простое число - это натуральное число, которое делится только на себя и на 1).
Выведите с помощью этой функции первые 20 простых чисел (начиная с 2) в одну строчку через пробел
"""

def prime_numbers(quantity):
    counter = 0
    generator = (number for number in range(2, 1_001))
    while counter < quantity:
        guess = next(generator)
        flag = 'Balakirev'

        for i in range(2, guess):
            if guess % i == 0:
                flag = 'Sergey'
                break

        if flag == 'Balakirev':
            counter += 1
            yield guess


N = 20
print(*prime_numbers(N))
