import tkinter as tk
from PIL import Image,ImageTk
import random

win = tk.Tk()

# words = ['word']
words = ['OBNOXIOUS','DEATH','HERO','TWENTY','THIRTY','FORTY','SIXTY']
ranwords = random.choice(words).lower()

image = Image.open("Sprite-0007.png")
tk_image = ImageTk.PhotoImage(image)
image1 = Image.open("Sprite-0006.png")
tk_image1 = ImageTk.PhotoImage(image1)
image2 = Image.open("Sprite-0005.png")
tk_image2 = ImageTk.PhotoImage(image2)
image3 = Image.open("Sprite-0004.png")
tk_image3 = ImageTk.PhotoImage(image3)
image4 = Image.open("Sprite-0003.png")
tk_image4 = ImageTk.PhotoImage(image4)
image5 = Image.open("Sprite-0002.png")
tk_image5 = ImageTk.PhotoImage(image5)
image6 = Image.open("Sprite-0001.png")
tk_image6 = ImageTk.PhotoImage(image6)

win.title('HANGMAN')
win.geometry('400x400')
win.resizable(False,False)
count = 0
hintcount = 0
guessed = []
hangman_dict = {
    0: '',
    1: tk_image,
    2: tk_image1,
    3: tk_image2,
    4: tk_image3,
    5: tk_image4,
    6: tk_image5,
    7: tk_image6
}


image = tk.PhotoImage()
label = tk.Label(win, image=image)
label.pack()

labelMistake = tk.Label(win,text=' ')
labelMistake.place(relx=0.5,rely=0.6,anchor=tk.CENTER)

labelword = tk.Label(win,text='_'*len(ranwords))
labelword.place(relx=0.5,rely=0.3,anchor=tk.CENTER)
def calculate_into_button(operation):
    return tk.Button(win, text=operation, bd=5, font=('Arial', 13), command=game)

def game():
    value = hangman.get()
    global count
    global ranwords
    global hintcount
    global guessed
    hangman.delete(0, tk.END)
    if set(ranwords) == set(guessed):
        print('You Win')
        exit()
    if count == 6:
        print('You lost')
        win.after(2000, win.destroy)
    elif value != ranwords and value not in ranwords and len(value) == 1 and not value in '1234567890':
        count+=1
        print(count, 'mistakes')
        label.config(image=hangman_dict[count])
    if value in '234567890':
        labelMistake.configure(text='Введите букву')
    if count > 2:
        labelMistake.configure(text='Для подсказки Нажмите 1')
    if len(value) > 1 and value != ranwords:
        labelMistake.configure(text='введите одну букву')
    if value == '1':
        if hintcount < len(ranwords) / 2:
            hintcount += 1
            labelMistake.configure(text=f'В слове есть буква  ({" ".join(random.choice(ranwords))})')
        else:
            labelMistake.configure(text='Подсказкой больше нельзя воспользоваться')
    elif value in ranwords:
        if len(value) == 1:
            labelMistake.configure(text='буква(ы) {} есть в слове'.format(', '.join(value)))
            guessed.append(value)
            guessed_word = ''
            for i in range(len(ranwords)):
                if ranwords[i] in guessed:
                    guessed_word += ranwords[i]
                else:
                    guessed_word += '_'
            labelword.configure(text=guessed_word)


hangman = tk.Entry(win, width=20)
hangman.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
calculate_into_button('Enter').place(relx=0.5, rely=0.5, anchor=tk.CENTER)


win.mainloop()











