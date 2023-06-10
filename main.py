# # Дана строчка, представляющая собой набор цифр.
# # И дано число от 0 до 19 (не включая).
# # Определить, присутсвуют ли в строчке 2 цифры,
# # такие, что сумма их равна введённому Вами числу?
# # Если да, то вывести эти цифры и  их индексы.
# someNumbers = int(input('введите набор цифр\n'))
# number = int(input('введите число от 0 до 18 включительно\n'))
# str1 = str(someNumbers)
# lenX = len(str1)
# z = 1
# x = 100
# c = 10
# while lenX > 0:
#     cnt1 = lenX + 1
#     cnt2 = cnt1 - 3
#     cnt3 = cnt1 - 2
#     number1 = someNumbers // z % 10
#     number2 = someNumbers // x % 10
#     number3 = someNumbers // c % 10
#     cnt1 -= 1
#     lenX -= 1
#     z *= 10
#     x *= 10
#     c *= 10
#     if number1 + number2 == number:
#         print(number1)
#         print(number2)
#         print(cnt1)
#         print(cnt2)
#     if number2 + number3 == number:
#         print(number2)
#         print(number3)
#         print(cnt2)
#         print(cnt3)
#     if number1 + number3 == number:
#         print(number1)
#         print(number3)
#         print(cnt1)
#         print(cnt3)
# else:
#     print('number not found')

# # Даны две строки. Эти строки между собой отличаются только одним символом.
# # Вторая строка получена путём добавления слуайного символа в случайную
# # позицию в первой строке.  Вывести данный символ и его индекс.
# someString1 = input('input some string1')
# someString2 = input('input some string2')
# lenSomeString1 = len(someString1)
# lenSomeString2 = len(someString2)
# while lenSomeString2 > -1:
#     z1 = int(lenSomeString1)
#     x1 = int(lenSomeString2)
#     z = someString1[z1-1]
#     x = someString2[x1-1]
#     lenSomeString2 -= 1
#     lenSomeString1 -= 1
#     if z != x:
#         print(x)
#         print(lenSomeString2 + 1)
#         break
# else:
#     print('введены идентичные строки')