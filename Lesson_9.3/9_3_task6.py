"""
9.3 Функция map (задача 6)
Подвиг 6. Вводятся названия городов в одну строчку через пробел. Необходимо определить функцию map,
которая бы возвращала названия городов только длиной более 5 символов. Вместо остальных названий - строку с дефисом ("-").
Сформировать список из полученных значений и отобразить его на экране в одну строчку через пробел.

Sample Input:
Москва Уфа Вологда Тула Владивосток Хабаровск

Sample Output:
Москва - Вологда - Владивосток Хабаровск
"""

cities = input().split()
result = list(map(lambda city: city if len(city) > 5 else '-', cities))
print(*result)
