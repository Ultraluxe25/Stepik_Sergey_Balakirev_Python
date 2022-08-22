""" 
7.11 Декораторы функций (Задача 4)
Подвиг 4. Вводятся две строки из слов (слова записаны через пробел).
Объявите функцию, которая преобразовывает эти две строки в два списка слов и возвращает эти списки.

Определите декоратор для этой функции, который из двух списков формирует словарь, в котором ключами являются слова из первого списка,
а значениями - соответствующие элементы из второго списка. Полученный словарь должен возвращаться при вызове декоратора.

Примените декоратор к первой функции и вызовите ее для введенных строк. Результат (словарь d) отобразите на экране командой:

print(*sorted(d.items()))

Sample Input:
house river tree car
дом река дерево машина

Sample Output:
('car', 'машина') ('house', 'дом') ('river', 'река') ('tree', 'дерево')
"""

english_words = input()
russian_words = input()


def decorator(function):
    def wrapper(rus, eng):
        eng_list, rus_list = function(rus, eng)       
        dictionary = dict()
        for index, word in enumerate(eng_list):
            dictionary[word] = rus_list[index]
            
        return dictionary
    
    return wrapper


@decorator
def converter(string_1, string_2):
    string_1 = string_1.split()
    string_2 = string_2.split()
    # print(string_1, string_2)
        
    return string_1, string_2


# converter(english_words, russian_words) 
print(*sorted(converter(english_words,russian_words).items()))
