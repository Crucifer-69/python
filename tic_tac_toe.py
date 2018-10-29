import sys
from random import randint
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

# global variables

activePlayer = 1
p1 = []
p2 = []
count = 0

root = Tk()
root.title('Tic Tac Toy')
# label
label = Label(root, text="player 1", relief=RAISED)
label.grid(row=0, column=1, sticky='snew', )
style = ttk.Style()
# buttons
bu1 = ttk.Button(root, text=' ')
bu1.grid(row=1, column=0, sticky='snew', ipadx=40, ipady=40, padx=1, pady=1)
bu1.config(command=lambda: ButtonClick(1))

bu2 = ttk.Button(root, text=' ')
bu2.grid(row=1, column=1, sticky='snew', ipadx=40, ipady=40, padx=1, pady=1)
bu2.config(command=lambda: ButtonClick(2))

bu3 = ttk.Button(root, text=' ')
bu3.grid(row=1, column=2, sticky='snew', ipadx=40, ipady=40, padx=1, pady=1)
bu3.config(command=lambda: ButtonClick(3))

bu4 = ttk.Button(root, text=' ')
bu4.grid(row=2, column=0, sticky='snew', ipadx=40, ipady=40, padx=1, pady=1)
bu4.config(command=lambda: ButtonClick(4))

bu5 = ttk.Button(root, text=' ')
bu5.grid(row=2, column=1, sticky='snew', ipadx=40, ipady=40, padx=1, pady=1)
bu5.config(command=lambda: ButtonClick(5))

bu6 = ttk.Button(root, text=' ')
bu6.grid(row=2, column=2, sticky='snew', ipadx=40, ipady=40, padx=1, pady=1)
bu6.config(command=lambda: ButtonClick(6))

bu7 = ttk.Button(root, text=' ')
bu7.grid(row=3, column=0, sticky='snew', ipadx=40, ipady=40, padx=1, pady=1)
bu7.config(command=lambda: ButtonClick(7))

bu8 = ttk.Button(root, text=' ')
bu8.grid(row=3, column=1, sticky='snew', ipadx=40, ipady=40, padx=1, pady=1)
bu8.config(command=lambda: ButtonClick(8))

bu9 = ttk.Button(root, text=' ')
bu9.grid(row=3, column=2, sticky='snew', ipadx=40, ipady=40, padx=1, pady=1)
bu9.config(command=lambda: ButtonClick(9))


def ButtonClick(id):
    global activePlayer
    global p1
    global p2

    if activePlayer == 1:
        SetLayout(id, "X")
        p1.append(id)
        label = Label(root, text="player 2", relief=RAISED)
        label.grid(row=0, column=1, sticky='snew')
        activePlayer = 2
        # print("p1:{}".format(p1))
        AutoPlay()

    elif activePlayer == 2:
        SetLayout(id, "O")
        p2.append(id)
        label = Label(root, text="player 1", relief=RAISED)
        label.grid(row=0, column=1, sticky='snew')
        activePlayer = 1
        # print("p2:{}".format(p2))
    CheckWinner()


def SetLayout(id, symbol):
    global count
    if id == 1:
        if symbol == "X":
            style.configure('red.TButton', background='red')
            bu1.configure(style="red.TButton")
        else:
            style.configure('blue.TButton', background='blue')
            bu1.configure(style="blue.TButton")
        bu1.config(text=symbol)
        bu1.state(['disabled'])
        count += 1
    elif id == 2:
        if symbol == "X":
            style.configure('red.TButton', background='red')
            bu2.configure(style="red.TButton")
        else:
            style.configure('blue.TButton', background='blue')
            bu2.configure(style="blue.TButton")
        bu2.config(text=symbol)
        bu2.state(['disabled'])
        count += 1
    elif id == 3:
        if symbol == "X":
            style.configure('red.TButton', background='red')
            bu3.configure(style="red.TButton")
        else:
            style.configure('blue.TButton', background='blue')
            bu3.configure(style="blue.TButton")
        bu3.config(text=symbol)
        bu3.state(['disabled'])
        count += 1
    elif id == 4:
        if symbol == "X":
            style.configure('red.TButton', background='red')
            bu4.configure(style="red.TButton")
        else:
            style.configure('blue.TButton', background='blue')
            bu4.configure(style="blue.TButton")
        bu4.config(text=symbol)
        bu4.state(['disabled'])
        count += 1
    elif id == 5:
        if symbol == "X":
            style.configure('red.TButton', background='red')
            bu5.configure(style="red.TButton")
        else:
            style.configure('blue.TButton', background='blue')
            bu5.configure(style="blue.TButton")
        bu5.config(text=symbol)
        bu5.state(['disabled'])
        count += 1
    elif id == 6:
        if symbol == "X":
            style.configure('red.TButton', background='red')
            bu6.configure(style="red.TButton")
        else:
            style.configure('blue.TButton', background='blue')
            bu6.configure(style="blue.TButton")
        bu6.config(text=symbol)
        bu6.state(['disabled'])
        count += 1
    elif id == 7:
        if symbol == "X":
            style.configure('red.TButton', background='red')
            bu7.configure(style="red.TButton")
        else:
            style.configure('blue.TButton', background='blue')
            bu7.configure(style="blue.TButton")
        bu7.config(text=symbol)
        bu7.state(['disabled'])
        count += 1
    elif id == 8:
        if symbol == "X":
            style.configure('red.TButton', background='red')
            bu8.configure(style="red.TButton")
        else:
            style.configure('blue.TButton', background='blue')
            bu8.configure(style="blue.TButton")
        bu8.config(text=symbol)
        bu8.state(['disabled'])
        count += 1
    elif id == 9:
        if symbol == "X":
            style.configure('red.TButton', background='red')
            bu9.configure(style="red.TButton")
        else:
            style.configure('blue.TButton', background='blue')
            bu9.configure(style="blue.TButton")
        bu9.config(text=symbol)
        bu9.state(['disabled'])
        count += 1


def CheckWinner():
    winner = -1
    # for rows
    # for p1
    if (1 in p1) and (2 in p1) and (3 in p1):
        winner = 1
    elif (4 in p1) and (5 in p1) and (6 in p1):
        winner = 1
    elif (7 in p1) and (8 in p1) and (9 in p1):
        winner = 1
    # for p2
    elif (1 in p2) and (2 in p2) and (3 in p2):
        winner = 2
    elif (4 in p2) and (5 in p2) and (6 in p2):
        winner = 2
    elif (7 in p2) and (8 in p2) and (9 in p2):
        winner = 2

    # for columns
    # for p1
    elif (1 in p1) and (4 in p1) and (7 in p1):
        winner = 1
    elif (2 in p1) and (5 in p1) and (8 in p1):
        winner = 1
    elif (3 in p1) and (6 in p1) and (9 in p1):
        winner = 1

    # for p2
    elif (1 in p2) and (4 in p2) and (7 in p2):
        winner = 2
    elif (2 in p2) and (5 in p2) and (8 in p2):
        winner = 2
    elif (3 in p2) and (6 in p2) and (9 in p2):
        winner = 2

    # for diagonals
    # for p2
    elif (1 in p1) and (5 in p1) and (9 in p1):
        winner = 1
    elif (3 in p1) and (5 in p1) and (7 in p1):
        winner = 1

    # for p2
    elif (1 in p2) and (5 in p2) and (9 in p2):
        winner = 2
    elif (3 in p2) and (5 in p2) and (7 in p2):
        winner = 2

    if winner == 1:
        bu1.state(['disabled'])
        bu2.state(['disabled'])
        bu3.state(['disabled'])
        bu4.state(['disabled'])
        bu5.state(['disabled'])
        bu6.state(['disabled'])
        bu7.state(['disabled'])
        bu8.state(['disabled'])
        bu9.state(['disabled'])
        messagebox.showinfo(title='congratulations', message="palyer 1 is the winner")
        sys.exit()

    elif winner == 2:
        bu1.state(['disabled'])
        bu2.state(['disabled'])
        bu3.state(['disabled'])
        bu4.state(['disabled'])
        bu5.state(['disabled'])
        bu6.state(['disabled'])
        bu7.state(['disabled'])
        bu8.state(['disabled'])
        bu9.state(['disabled'])
        messagebox.showinfo(title='congratulations', message="palyer 2 is the winner")
        sys.exit()

    elif count == 9:
        label = Label(root, text="No Winner", relief=RAISED)
        label.grid(row=0, column=1, sticky='snew')
        messagebox.showinfo(title='Draw', message="The match was a draw")
        sys.exit()


def AutoPlay():
    global p1
    global p2
    emptyCell = []
    for cell in range(9):
        if not ((cell + 1 in p1) or (cell + 1 in p2)):
            emptyCell.append(cell + 1)

    #auto play for p2
    if (1 in p2) and (2 in p2) and (3 in emptyCell):
        ButtonClick(3)
    elif (1 in p2) and (3 in p2) and (2 in emptyCell):
        ButtonClick(2)
    elif (2 in p2) and (3 in p2) and (1 in emptyCell):
        ButtonClick(1)

    elif (4 in p2) and (5 in p2) and (6 in emptyCell):
        ButtonClick(6)
    elif (5 in p1) and (6 in p2) and (4 in emptyCell):
        ButtonClick(4)
    elif (6 in p2) and (4 in p2) and (5 in emptyCell):
        ButtonClick(5)

    elif (7 in p2) and (8 in p2) and (9 in emptyCell):
        ButtonClick(9)
    elif (8 in p2) and (9 in p2) and (7 in emptyCell):
        ButtonClick(7)
    elif (9 in p2) and (7 in p2) and (8 in emptyCell):
        ButtonClick(8)

    # for columns
    elif (1 in p2) and (4 in p2) and (7 in emptyCell):
        ButtonClick(7)
    elif (4 in p2) and (7 in p2) and (1 in emptyCell):
        ButtonClick(1)
    elif (7 in p2) and (1 in p2) and (4 in emptyCell):
        ButtonClick(4)

    elif (2 in p2) and (5 in p2) and (8 in emptyCell):
        ButtonClick(8)
    elif (5 in p2) and (8 in p2) and (2 in emptyCell):
        ButtonClick(2)
    elif (8 in p2) and (2 in p2) and (5 in emptyCell):
        ButtonClick(5)

    elif (3 in p2) and (6 in p2) and (9 in emptyCell):
        ButtonClick(9)
    elif (6 in p2) and (9 in p2) and (3 in emptyCell):
        ButtonClick(3)
    elif (9 in p2) and (3 in p2) and (6 in emptyCell):
        ButtonClick(6)

    # for diagonals
    elif (1 in p2) and (5 in p2) and (9 in emptyCell):
        ButtonClick(9)
    elif (5 in p2) and (9 in p2) and (1 in emptyCell):
        ButtonClick(1)
    elif (9 in p2) and (1 in p2) and (5 in emptyCell):
        ButtonClick(5)

    elif (3 in p2) and (5 in p2) and (7 in emptyCell):
        ButtonClick(7)
    elif (5 in p2) and (7 in p2) and (3 in emptyCell):
        ButtonClick(3)
    elif (7 in p2) and (3 in p2) and (5 in emptyCell):
        ButtonClick(5)

    # auto play check for p1
    elif (1 in p1) and (2 in p1) and (3 in emptyCell):
        ButtonClick(3)
    elif (1 in p1) and (3 in p1) and (2 in emptyCell):
        ButtonClick(2)
    elif (2 in p1) and (3 in p1) and (1 in emptyCell):
        ButtonClick(1)

    elif (4 in p1) and (5 in p1) and (6 in emptyCell):
        ButtonClick(6)
    elif (5 in p1) and (6 in p1) and (4 in emptyCell):
        ButtonClick(4)
    elif (6 in p1) and (4 in p1) and (5 in emptyCell):
        ButtonClick(5)

    elif (7 in p1) and (8 in p1) and (9 in emptyCell):
        ButtonClick(9)
    elif (8 in p1) and (9 in p1) and (7 in emptyCell):
        ButtonClick(7)
    elif (9 in p1) and (7 in p1) and (8 in emptyCell):
        ButtonClick(8)

    # for columns
    elif (1 in p1) and (4 in p1) and (7 in emptyCell):
        ButtonClick(7)
    elif (4 in p1) and (7 in p1) and (1 in emptyCell):
        ButtonClick(1)
    elif (7 in p1) and (1 in p1) and (4 in emptyCell):
        ButtonClick(4)

    elif (2 in p1) and (5 in p1) and (8 in emptyCell):
        ButtonClick(8)
    elif (5 in p1) and (8 in p1) and (2 in emptyCell):
        ButtonClick(2)
    elif (8 in p1) and (2 in p1) and (5 in emptyCell):
        ButtonClick(5)

    elif (3 in p1) and (6 in p1) and (9 in emptyCell):
        ButtonClick(9)
    elif (6 in p1) and (9 in p1) and (3 in emptyCell):
        ButtonClick(3)
    elif (9 in p1) and (3 in p1) and (6 in emptyCell):
        ButtonClick(6)

    # for diagonals
    elif (1 in p1) and (5 in p1) and (9 in emptyCell):
        ButtonClick(9)
    elif (5 in p1) and (9 in p1) and (1 in emptyCell):
        ButtonClick(1)
    elif (9 in p1) and (1 in p1) and (5 in emptyCell):
        ButtonClick(5)

    elif (3 in p1) and (5 in p1) and (7 in emptyCell):
        ButtonClick(7)
    elif (5 in p1) and (7 in p1) and (3 in emptyCell):
        ButtonClick(3)
    elif (7 in p1) and (3 in p1) and (5 in emptyCell):
        ButtonClick(5)
    elif len(emptyCell) > 1:
        rIndex = randint(0, len(emptyCell) - 1)
        ButtonClick(emptyCell[rIndex])
        del emptyCell[rIndex]

    print(emptyCell)


root.mainloop()
