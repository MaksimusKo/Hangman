import random
print('Это словесная угадайка, у вас есть 6 попыток что бы угадать слово')

#words = ['WHAT','секретарь','знакомый','войско','звезда','двор','бутылка','чувство','этап','сердце','честь']
words = ['OBNOXIOUS','DEATH','HERO','TWENTY','THIRTY','FORTY','SIXTY']
# words = ['BARABARABARA']
ranwords = random.choice(words).lower()
hangman_dict = {
    0: '',
    1: '__________\n|         |\n|\n|\n|\n|',
    2: '__________\n|         |\n|         O\n|\n|\n|',
    3: '__________\n|         |\n|         O\n|         |\n|\n|',
    4: '__________\n|         |\n|         O\n|        /|\n|\n|',
    5: '__________\n|         |\n|         O\n|        /|\\\n|\n|',
    6: '__________\n|         |\n|         O\n|        /|\\\n|        /\n|',
    7: '__________\n|         |\n|         O\n|        /|\\\n|        / \\\n|'
}

def play():
    guessed = []
    wrong = []
    word = '_'*len(ranwords)
    wordds = list(word)
    count = 1
    hintcount = 0
    print('Подсказка, в слове', len(ranwords), 'буквы')
    print('Если вы хотите ещё подсказку нажмите 1')
    while count <= 6:
        guess = input()
        if count == 6:
            print('Вы проиграли')
            print(hangman_dict.get(7))
            exit()
        if guess in wrong or guess in guessed:
            print('Вы уже вводили эту букву')
        if len(guess) > 1 and guess != ranwords:
            print('введите одну букву')
        if guess in '234567890':
            print('Введите букву')
        elif guess in ranwords:
            if len(guess) == 1:
                print('буква(ы)', guess, 'есть в слове')
                guessed.append(guess)
                for i in range(len(ranwords)):
                    if ranwords[i] == guess:
                        wordds[i] = guess
                print('ваше слово', ''.join(wordds))
        if guess == ranwords or ''.join(wordds) == ranwords:
            print('Вы победили')
            exit()
        if guess != ranwords and guess not in ranwords and guess not in wrong and len(guess) == 1 and not guess in '1234567890':
            print('Неправильный ввод')
            print('ваше слово', ''.join(wordds))
            count += 1
            wrong.append(guess)
            if count in hangman_dict:
                print(hangman_dict[count]) #сама виселица
        if guess == '1':
            if hintcount < len(ranwords) / 2:
                hintcount += 1
                print('в слове есть буква', random.choice(ranwords))
            else:
                print('Подсказкой больше нельзя воспользоватся')


play()
