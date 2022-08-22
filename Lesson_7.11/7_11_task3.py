""" 
7.11 Декораторы функций (Задача 3)
Подвиг 3. На вход программы поступает строка из целых чисел, записанных через пробел.
Напишите функцию get_list, которая преобразовывает эту строку в список из целых чисел и возвращает его.
Определите декоратор для этой функции, который сортирует список чисел по возрастанию.
Результат сортировки должен возвращаться при вызове декоратора.

Вызовите декорированную функцию get_list и отобразите полученный отсортированный список lst командой:

print(*lst)

Sample Input:
8 11 -5 4 3 10

Sample Output:
-5 3 4 8 10 11
"""

def decorator(function):
    def wrapper(*args, **kwargs):
        return sorted(function(*args))
    
    return wrapper
        

@decorator
def get_list(numbers):
    numbers = list(map(int, numbers.split()))
    return numbers


lst = get_list(input())
print(*lst)
