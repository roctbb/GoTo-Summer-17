word = input("введи слово:")
words = []
words.append(word)
while True:
    last_char = word[-1]
    new_word = input("тебе на {0}:".format(last_char.upper())).lower()
    while not new_word.startswith(last_char) or new_word in words:
        print("Неверно!")
        new_word = input("тебе на {0}:".format(last_char.upper())).lower()
    word = new_word
    print("Следующий ход!")

