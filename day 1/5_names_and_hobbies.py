from random import choice

s =  ["Вася", "Миша", "Катя", "Света"]
hobbies = ["слушать музыку", "сидеть на дваче", "играть в компухтер", "петь Летова"]


for name in s[::-1]:
    print("{0} любит {1}. Такая уж она, эта {0}.".format(name, choice(hobbies)))

