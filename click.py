from tkinter import *
from tkinter import messagebox
from random import *

okno = Tk()
okno.title("Click")
okno.geometry("1280x720")
okno.resizable(width=False, height=False)
okno["background"] = "black"

clicks = 0

show = Label(okno, text='0', font=("Comic Sans MS", 20, 'underline'), bg='black', fg='white')
show.pack()


def move():
    global clicks
    clc.place(x=randint(70, 1000), y=randint(70, 650))
    clicks += 1
    show['text'] = str(clicks)
    show.pack()


clc = Button(okno, command=move, text='Click',
             bg='lime', fg='black',
             padx=16, pady=16,
             font=("Comic Sans MS", 20, 'underline'))
clc.place(x=randint(70, 1028), y=randint(70, 628))

okno.mainloop()
