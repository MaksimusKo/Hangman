import random
print('Это словесная угадайка, у вас есть 6 попыток что бы угадать слово')

#words = ['WHAT','секретарь','знакомый','войско','звезда','двор','бутылка','чувство','этап','сердце','честь']
words = ['OBNOXIOUS','DEATH','HERO','TWENTY','THIRTY','FORTY','SIXTY']
ranwords = random.choice(words).lower()
Hangman1 = (
    """
     ------
     |    |
     |    O
     |   /|\\
     |   / \\
     |   
     |   
    ----------
    """
)
Hangman2= (    """
     ------
     |    |
     |    O
     |   /|\\
     |   / 
     |   
     |   
    ----------
    """)
Hangman3=(    """
     ------
     |    |
     |    O
     |   /|\\
     |   
     |   
     |   
    ----------
    """)
Hangman4= (    """
     ------
     |    |
     |    O
     | 
     |  
     |   
     |   
    ----------
    """)
Hangman5= (    """
     ------
     |    |
     |    
     |  
     |   
     |   
     |   
    ----------
    """)
Hangman6= (    """
     ------
     |    
     |   
     |   
     |   
     |   
     |   
    ----------
    """)
def play():
    guessed = []
    wrong = []
    count = 1
    hintcount = 0
    print('Подсказка, в слове', len(ranwords), 'буквы')
    print('Если вы хотите ещё подсказку нажмите 1')
    while count <= 6:
        guess = input()
        if count == 6:
            print('Вы проиграли')
            print(Hangman1)
            exit()
        if guess in wrong or guess in guessed:
            print('Вы уже вводили эту букву')
        if len(guess) > 1 and guess != ranwords:
            print('введите одну букву')
        if guess in '234567890':
            print('Введите букву')
        elif guess in ranwords:
            if len(guess) == 1:
                print('буква', guess, 'есть в слове')
                guessed.append(guess)
                print('ваши угаданные буквы', guessed, )
                print('буква',guess,ranwords.index(guess)+1,'буква в слове')
        if guess == ranwords:
            print('Вы победили')
            exit()
        if guess != ranwords and guess not in ranwords and guess not in wrong and len(guess) == 1 and not guess in '1234567890':
            print('Неправильный ввод')
            print('ваши угаданные буквы', guessed, )
            count += 1
            wrong.append(guess)
            if count == 1:
                print(Hangman6)
            elif count == 2:
                print(Hangman5)
            elif count == 3:
                print(Hangman4)
            elif count == 4:
                print(Hangman3)
            elif count == 5:
                print(Hangman2)
        if guess == '1':
            if hintcount < len(ranwords) / 2:
                hintcount += 1
                print('в слове есть буква', random.choice(ranwords))
            else:
                print('Подсказкой больше нельзя воспользоватся')


play()
