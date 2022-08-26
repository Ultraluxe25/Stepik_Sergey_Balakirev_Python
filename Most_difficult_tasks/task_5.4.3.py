""" 
5.4 Примеры работы оператора цикла for. Функция enumerate (Задача 3)
Большой подвиг 3. В виде строки записано арифметическое выражение, например:

"10 + 25 - 12"

или

"10 + 25 - 12 + 20 - 1 + 3"

и т. д. То есть, количество действий может быть разным.

Необходимо выполнить вычисление и результат отобразить на экране.
Полагается, что в качестве арифметических операций здесь используется только сложение (+) и вычитание (-), а в качестве операндов - целые неотрицательные числа.
Следует учесть, что эти операторы могут быть записаны как с пробелами, так и без них.

Sample Input:
10+25 - 12

Sample Output:
23
"""

math = input()

result = math.replace(' ', '').replace('-', '+-')
result = result.split('+')

for i in range(len(result)):
    result[i] = int(result[i])
    
print(sum(result))