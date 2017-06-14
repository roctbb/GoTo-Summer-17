import random

a = random.randint(1,20)

while True:
    v = int(input("Введи число: "))
    if v != a:
        print("Azazaz")
    else:
        break


print("Вы угадали!")
