"""
9.4 Функция map (задача 5)
Подвиг 5. Вводится список email-адресов в одну строчку через пробел. Среди них нужно оставить только корректно записанные адреса.
Будем полагать, что к таким относятся те, что используют латинские буквы, цифры и символ подчеркивания.
А также в адресе должен быть символ "@", а после него символ точки "." (между ними, конечно же, могут быть и другие символы).

Результат отобразить в виде строки email-адресов, записанных через пробел.

Sample Input:
abc@it.ru dfd3.ru@mail biba123@list.ru sc_lib@list.ru $fg9@fd.com

Sample Output:
abc@it.ru biba123@list.ru sc_lib@list.ru
"""

from string import ascii_lowercase, ascii_uppercase
correct_chars = ascii_lowercase + ascii_uppercase + '1234567890_.@'


def email_check(email):
        if email.count('@') != 1 or email.count('.') != 1:
            return False
        elif email.index('.') < email.index('@'):
            return False

        for char in email:
            if char not in correct_chars:
                return False
            
        return True

    
emails = input().split()
print(*tuple(filter(email_check, emails)))
