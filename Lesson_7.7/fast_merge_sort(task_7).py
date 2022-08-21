""" 
7.7 Рекурсивные функции (Задача 7)
Великий подвиг 8. Вводится список из целых чисел в одну строчку через пробел.
Необходимо выполнить его сортировку по возрастанию с помощью алгоритма сортировки слиянием. Функция должна возвращать новый отсортированный список.
Вызовите результирующую функцию сортировки для введенного списка и отобразите результат на экран в виде последовательности чисел, записанных через пробел.

Подсказка. Для разбиения списка и его последующей сборки используйте рекурсивные функции.

P. S. Теория сортировки в видео предыдущего шага. 
https://www.youtube.com/watch?v=SnzZ61aCVxc&list=PLA0M1Bcd0w8yF0PO0eJ9v8VlsYEowmsnJ&index=13

Sample Input:
8 11 -6 3 0 1 1

Sample Output:
-6 0 1 1 3 8 11
"""

def slow_merge_sort(list_1, list_2):
    common_list = []
    # указатели списков
    i = 0
    j = 0

    # длины списков для индексов
    length_list_1 = len(list_1)
    length_list_2 = len(list_2)

    while i < length_list_1 and j < length_list_2:
        if list_1[i] < list_2[j]:
            common_list.append(list_1[i])
            i += 1
        else:  # list_1[i] >= list_2[j]
            common_list.append(list_2[j])
            j += 1

    common_list += list_1[i:] + list_2[j:]

    return common_list


def fast_merge_sort(whole_list):
    middle = len(whole_list) // 2
    part_1 = whole_list[:middle]
    part_2 = whole_list[middle:]

    # разбивание списка на списки из одного элемента
    if len(part_1) > 1:
        # рекурсионное деление списка
        part_1 = fast_merge_sort(part_1)

    if len(part_2) > 1:
        part_2 = fast_merge_sort(part_2)

    return slow_merge_sort(part_1, part_2)


numbers = list(map(int, input().split()))
result = fast_merge_sort(numbers)
print(*result)
