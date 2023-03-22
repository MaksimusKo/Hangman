import random
print('Это словесная угадайка, у вас есть 6 попыток что бы угадать слово')

#words = ['WHAT','секретарь','знакомый','войско','звезда','двор','бутылка','чувство','этап','сердце','честь']
words = ['what']
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
    guessed = ['']
    wrong = []
    count = 1
    while count <= 6:
        guess = input()
        if count == 6:
            print('Вы проиграли')
            print(Hangman1)
            exit()
        if guess in wrong or guess in guessed:
            print('Вы уже вводили эту букву')
        if len(guess) > 1:
            print('введите одну букву')
        elif guess in ranwords:
            if len(guess) == 1:
                print('буква', guess, 'есть в слове')
                guessed[0] = guessed[0]+guess
                print('ваши угаданные буквы', guessed, )
        if guess == ranwords:
            print('Вы победили')
            exit()
        if guess != ranwords and guess not in ranwords and guess not in wrong and len(guess) == 1:
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


play()
