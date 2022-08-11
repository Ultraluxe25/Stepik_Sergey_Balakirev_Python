"""
9.4 Функция map (задача 4)
Подвиг 4. Саша и Галя коллекционируют монетки. Каждый из них решил записать номиналы монеток из своей коллекции.
Получилось два списка. Эти списки поступают на вход программы в виде двух строк из целых чисел, записанных через пробел.
Необходимо выделить значения, присутствующие в обоих списках и оставить среди них только четные.
Результат вывести на экран в виде строки полученных чисел в порядке их возрастания через пробел.

При реализации программы используйте функцию filter и кое-что еще (для упрощения программы), подумайте что.

Sample Input:
1 5 2 7 10 25 50 100
5 2 3 7 10 25 55

Sample Output:
2 10
"""

Sasha = tuple(map(int, input().split()))
Galya = tuple(map(int, input().split()))

# common_numbers = list()

# for number in Sasha:
#    if number in Galya and number not in common_numbers:
#        common_numbers.append(number)
        
# for number in Galya:
#    if number in Sasha and number not in common_numbers:
#        common_numbers.append(number)

# even_common_numbers = tuple(filter(lambda number: number % 2 == 0, common_numbers))
# print(*even_common_numbers)

print(*(sorted(filter(lambda number: number % 2 == 0, tuple(filter(lambda x: x in Sasha, Galya))))))
