""" 
5.4 Примеры работы оператора цикла for. Функция enumerate (Задача 2)
Подвиг 2. Вводится строка с номером телефона. Ожидается формат ввода:

+7(xxx)xxx-xx-xx

где x - это цифра. Размер введенных символов считается верным (то есть, не может быть, чтобы отсутствовала какая-либо цифра или была лишняя).
Необходимо проверить, что введенная строка соответствует этому формату. Вывести ДА, если соответствует и НЕТ - в противном случае.

Sample Input:
+7(123)456-78-99

Sample Output:
ДА
"""

n = input()
# symb = [0, 2, 6, 10, 13]
ans = "ДА"

if n[:3] == '+7(' and n[6] == ')' and n[10] == n[13] == '-':
    numbers = n[3:6] + n[7:10] + n[11:13] + n[14:]

    for i in range(len(numbers)):

#   for i in range(len(n)):
#   if i == 0 or i == 2 or i == 6 or i == 10 or i == 13:

        if numbers[i] not in '1234567890':
            ans = 'НЕТ'
            break

#       i += 1
#       #continue
#  else:
#    if n[0] == "+" and n[2] == "(" and n[6] == ")" and n[10] == "-" or n[10] == " " and n[13] == "-" or n[13] == " " and:

else:
    ans = "НЕТ"

print(ans)
