"""
9.4 Функция map (задача 1)
Подвиг 1. Вводятся названия городов в одну строчку через пробел.
Необходимо определить функцию filter, которая бы возвращала только названия длиной более 5 символов.
Извлеките первые три полученных значения с помощью функции next и отобразите их на экране в одну строчку через пробел.
(Полагается, что минимум три значения имеются).

Sample Input:
Тула Ульяновск Хабаровск Владивосток Омск Уфа

Sample Output:
Ульяновск Хабаровск Владивосток
"""

cities = input().split()
long_name_cities = filter(lambda city: len(city) > 5, cities)

for _ in range(3):
    print(next(long_name_cities), end=' ')