"""
9.4 Функция map (задача 3)
Подвиг 3. Вводится список целых чисел в одну строчку через пробел. Необходимо оставить в нем только двузначные числа.
Реализовать программу с использованием функции filter. Результат отобразить на экране в виде последовательности оставшихся чисел в одну строчку через пробел.

Sample Input:
8 11 0 -23 140 1

Sample Output:
11 -23
"""

# print(*list(filter(lambda number: abs(number) > 9 and abs(number) < 100, map(int, input().split()))))

all_numbers = tuple(map(int, input().split()))
numbers = filter(lambda number: 9 < abs(number) < 100, all_numbers)

for number in numbers:
    print(number, end=' ')
