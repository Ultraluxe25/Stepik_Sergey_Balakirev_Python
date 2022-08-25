""" 
9.6 Сортировка с помощью sort и sorted (Задача 1)
Подвиг 5. На вход программы поступают два списка целых чисел (каждый в отдельной строке), записанных в одну строчку через пробел.
Длины списков могут быть разными. Необходимо первый список отсортировать по возрастанию, а второй - по убыванию.
Полученные пары из обоих списков сложить друг с другом и получить новый список чисел. Результат вывести на экран в виде строки чисел через пробел.

P. S. Подсказка: не забываем про функцию zip.

Sample Input:
7 6 4 2 6 7 9 10 4
-4 5 10 4 5 65

Sample Output:
67 14 9 11 10 3
"""

numbers1 = list(map(int, input().split()))
numbers2 = list(map(int, input().split()))

numbers1.sort()
numbers2.sort(reverse=True)

# union_numbers = []
#
# if len(numbers1) < len(numbers2):
#     for index, value in enumerate(numbers1):
#        union_numbers.append(value + numbers2[index])
# else:
#     for index, value in enumerate(numbers2):
#         union_numbers.append(value + numbers1[index])
#
# print(*union_numbers)

union_numbers = list(zip(numbers1, numbers2))

for index, value in enumerate(union_numbers):
    union_numbers[index] = sum(value)
print(*union_numbers)
