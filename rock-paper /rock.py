from tkinter import *
from tkinter import ttk
import random

# Call a new window
root = Tk()

# Set a name for the window
root.title('Test')
root.resizable(0, 0)

# Set the size of the window
root.geometry('400x400')
root.config(bg='seashell3')


Label(root, text='rock, Paper, Scissors',
      font='arial 20 bold', bg='seashell2', fg='#000').pack()

# User Choice

user_take = StringVar()
Label(root, text='Choose your rock, paper scissors',
      font='arial 15 bold', bg='seashell2').place(x=90, y=70)
Entry(root, font='arial 15', textvariable=user_take,
      bg='antiquewhite2', fg='#000').place(x=90, y=130)


# Play Function

Result = StringVar()


def play():
    # reset the computer pick everytime
    comp_result = random.randint(1, 3)
    if comp_result == 1:
        comp_result = 'rock'
    elif comp_result == 2:
        comp_result = 'paper'
    elif comp_result == 3:
        comp_result = 'scissors'

    user_pick = user_take.get()
    if user_pick == comp_result:
        Result.set('tie,you both select same')
    elif user_pick == 'rock' and comp_result == 'paper':
        Result.set('you loose,computer select paper')
    elif user_pick == 'rock' and comp_result == 'scissors':
        Result.set('you win,computer select scissors')
    elif user_pick == 'paper' and comp_result == 'scissors':
        Result.set('you loose,computer select scissors')
    elif user_pick == 'paper' and comp_result == 'rock':
        Result.set('you win,computer select rock')
    elif user_pick == 'scissors' and comp_result == 'rock':
        Result.set('you loose,computer select rock')
    elif user_pick == 'scissors' and comp_result == 'paper':
        Result.set('you win ,computer select paper')
    else:
        Result.set('invalid: choose any one -- rock, paper, scissors')

# define reset functions & and set those string value to empty


def reset():
    Result.set("")
    user_take.set("")


# define quit function

def exit():
    root.destroy()

# Define  buttons


Entry(root, textvariable=Result, bg="antiquewhite2",
      font="arial 10 bold", width="50", fg="#000").place(x=25, y=250)
Button(root, font='arial 13 bold', text='PLAY', padx=5,
       bg='seashell4', command=play).place(x=150, y=190)
Button(root, font='arial 13 bold', text='RESET', padx=5,
       bg='seashell4', command=reset).place(x=70, y=310)
Button(root, font='arial 13 bold', text='EXIT', padx=5,
       bg='seashell4', command=exit).place(x=230, y=310)


root.mainloop()
