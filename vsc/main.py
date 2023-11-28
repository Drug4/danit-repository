# print(7)
# x=7

# print(x)

# x=10

# user_name=input("Привет, введи свое имя: ")

# print("Привет,рад тебя видеть",user_name)

# first_number=int(input("ведите первое число"))

# second_number=int(input("ведите второе число"))

# result=first_number+second_number

# print(result)

# #! Розгалудження
# user_number=int(input("ведите число"))


# if user_number % 2==0:
#     print("Вамше число парное")
# else:
#     print("Ваше число не парне")

#     #! Логические операторы 

# '''
# - логичное И: and
# - логичное ИЛИ: or
# - логичное НЕ:not
# '''

# print(not True)
# print(not False)
# print(not not True)
# print(not not False)
# print(bool(" "))

# print(10 or 0 or False)
# print(None or "" or "hello" or 0)

# print("hello" and "python" and 158 and None and -59)
# print("hey" and 0 and "" and False and "python")

# '''
# first_number = int(input("Введіть перше число: "))
# second_number = int(input("Введіть друге число: "))
# operation = input("Введіть знак операції: ")

# result = 0

# if operation == "+":
#     result = first_number + second_number
# elif operation == "-":
#     result = first_number - second_number
# elif operation == "*":
#     result = first_number * second_number
# elif operation == "/":
#     result = first_number / second_number
# else:
#     result = "Неправильна операція"

# print("Результат:", result)


# '''
# print("Введіть 3 числа: ")
# num1 = int(input())
# num2 = int(input())
# num3 = int(input())

# biggest_num = num1

# if num1 > num2 and num1 > num3:
#     biggest_num = num1
# elif num2 > num1 and num2 > num3:
#     biggest_num = num2
# else:
#     biggest_num = num3

# print("Число", biggest_num, "найбільше")



 


 '''
# word = "hello"

# for letter in word:
#     print(letter)
'''
# range(a, b) -> [a, b)
# range(1, 10) -> 1, 2, 3, 4, 5, 6, 7, 8, 9
# range(5, 8) -> 5, 6, 7

# range(1, 11, 3) -> 1, 4, 7, 10

'''
# sentence = "H5el5lo5 e5v5er5yo5ne5!5 N5i5ce5 t5o 5m5e5e5t5 y5o5u5"
# correctSentence = "" # "Hello everyone! Nice to meet you"
'''



# for char in sentence:
    # if char!="5":
        # correctSentence += char

# print(correctSentence)
'''
'''
#word = input("Введіть слово: ")
#letter = input("Введіть букву, яку хочете знайти: ")

#for char in word:
#    if char == letter:
#        print("Буква", letter, "є у слові", word)
#        break
#else:
#   print("Букви", letter, "немає у слові", word)
'''
'''
from_number = int(input("введите начало диапозона"))
to_number = int(input("введите конец диапозона"))+1

while from_number>=to_number:
    to_number = int(input("не верно!правая сторона не может быть меньше левой,попробуйте еще раз!"))+1
search_number = int(input("введите число которое хотите проверить:"))
for number in range(from_number, to_number):
    if search_number ==number:
        print("Число", search_number, "есть в диапозоне")
        break
else:
    print("Числа", search_number, "нет в диапозоне")
'''

#word = "Jojo fast speedrun"
#for letter in word:
#    print (letter)


 cash = int(input("Внесите Деньги"))
 print("Выберите товар: \n 1 - Плюш.игр.(200 грн),\n 2 - Пластик.игр.(300 грн):")
 toy = int(input())

 if toy = 1 and cash =>200:
        print("вот ваша игрушка,ваша сдача -:")
 elif toy = 2 and cash =>300:
   print("вот ваша игрушка,ваша сдача -", cash - 300, "грн")
 elif toy = 2 and cash =>300:
    print("вот ваша игрушка, ваша сдача -", cash - 300, "грн")
 else:
    print("Ошибка!Заберите ваши деньги")

 

cash = int(input("Внесите Деньги"))
 print("Виберіть напій: \n 1 - Лате(25 грн), \n 2 - Капучино(50 грн), \n 3 - Чай (10 грн):")
 drink = int(input())

 if drink = 1 and cash =>25:
         print("вот ваше лате,заберите сдачу")
 elif drink = 2 and cash =>50
  print("Ось ваш Лате, ваша решта -", cash - 25, "грн")
 elif drink = 2 and cash =>50
  print("Ось ваш Лате, ваша решта -", cash - 25, "грн")
 elif drink == 3 and cash >= 10:
     print("Ось ваш Чай, ваша решта -", cash - 10, "грн")
 else:
     print("Помилка! Заберіть ваші кошти!")


