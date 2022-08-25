""" 
9.6 Сортировка с помощью sort и sorted (Задача 3)
Подвиг 4. На вход программы поступает список целых чисел, записанных в одну строчку через пробел.
Необходимо выбрать из них четыре наибольших уникальных значения. Результат вывести на экран в порядке их убывания в одну строчку через пробел.

Sample Input:
10 5 4 -3 2 0 5 10 3

Sample Output:
10 5 4 3
"""

numbers = list(map(int, input().split()))
unique_numbers = sorted(set(numbers), reverse=True)
print(*unique_numbers[:4])