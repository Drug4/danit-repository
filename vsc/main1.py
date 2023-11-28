# cash = int(input("Внесите Деньги"))
# print("Выберите товар: \n 1 - Плюш.игр.(200 грн),\n 2 - Пластик.игр.(300 грн):")
# toy = int(input())

# if toy == 1 and cash >=200:
#     print("вот ваша игрушка,ваша сдача -:",cash - 200, "грн")
# elif toy == 2 and cash >=300:
#    print("вот ваша игрушка,ваша сдача -", cash - 300, "грн")
# else:
#     print("Ошибка!Заберите ваши деньги")


#def sum(n, m):
 #   return n + m

#print(sum(2, 68))

# word = "таракан Вадим"
# for letter in word:
#     print (letter)

# def str_length(str):
# counter = 0
# for char in str:
#     counter += 1 # counter = counter + 1
# return counter


# print(str_length("hello!"))  # 6
# print(str_length("hello, my name is Alex")) # 22


# def reverseStr(str):
#     # code
#     return


# word = "hello"
# for letter in word:
#      print (letter)
# print(reverseStr("hello")) # olleh

# def reverseStr(str):
#     new_str = ""
#     str_len = len(str) # 5
#     for i in range(str_len): # 0 до 4
#         new_str += str[str_len - i - 1]
#         #1 str[5 - 0 - 1] -> str[4] -> o
#         #2 str[5 - 1 - 1] -> str[3] -> l
#         #3 str[5 - 2 - 1] -> str[2] -> l
#         #4 str[5 - 3 - 1] -> str[1] -> e
#         #5 str[5 - 4 - 1] -> str[0] -> h
#     return new_str
#     print(reverseStr("hello")) # olleh
# print(reverseStr("laptop")) # potpal
# print(reverseStr("привіт")) # тівирп
    
#
# import random
# def get_random_int(min, max):
#     return random.randint(min, max)

# print(get_random_int(100, 500))

# import tkinter as tk

# def get_text():
#     label["text"] = message.get()

# window = tk.Tk()  # створення головного елементу інтерфейсу - вікна

# window.title("Це заголовок моєї програми")  # створює заголовок вікна програми

# # задаємо розміри та відстпупи вікна: 400 - ширина, 200 - висота, 450 - відступ зліва, 300 - відступ зправа
# window.geometry("400x200+450+300")
# window.configure(bg="red")
# greeting = tk.Label(text="Hello, world!", bg="yellow",
#                     fg="orange", font="Arial 48 bold")

# greeting.pack()  # розмістити віджет на вікні
# message = tk.StringVar() # контейнер для нашого тексту
# entry = tk.Entry(textvariable=message)
# entry.pack()
# label = tk.Label(text="Тут буде ваш текст")
# label.pack()

# tk.Button(text="Click", command=get_text).pack()

# window.mainloop()  # це нескінченний цикл, який не дає нашій програмі закритись
import tkinter as tk

import random
def get_random_int(min, max):
     return random.randint(min, max)


def update_number():
    label["text"] = get_random_int(0, 200)

window = tk.Tk()

window.title("это генератор рандомного числа")

window.geometry("200x200+600+400")

window.title("это заголовок рандомайзера")
label = tk.Label(text = "Ваше число")
label.pack()
tk.Button(text="Click", command = update_number).pack()

window.mainloop()







