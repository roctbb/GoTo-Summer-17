temp = int(input("Сколько градусов?"))
rain = input("Идет дождь (да/нет)?")

if temp > 20 and rain == "нет":
    print("Иди гуляй, че как сыч сидишь!")
elif temp > 15 and rain == "нет":
    print("Можно выйти на балкон")
else:
    print("Учись сиди! Вот ерохин уже сколько зарабатывает! Машину тете Глаше купил!")
