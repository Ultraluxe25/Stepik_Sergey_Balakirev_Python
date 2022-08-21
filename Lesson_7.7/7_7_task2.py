""" 
7.7 Рекурсивные функции (Задача 2)
Подвиг 3. Вводится список целых чисел в одну строчку через пробел. Необходимо вычислить сумму этих введенных значений, используя рекурсивную функцию (для перебора элементов списка) с именем get_rec_sum. Функция должна возвращать значение суммы. (Выводить на экран она ничего не должна).

Вызовите эту функцию и выведите вычисленное значение суммы на экран.

Sample Input:
8 11 -5 4 3

Sample Output:
21
"""

def sum_numbers(numbers):
    if not numbers:
        return 0
    else:
        return numbers[0] + sum_numbers(numbers[1:])
        

numbers = list(map(int, input().split()))
print(sum_numbers(numbers))
