from tkinter import ttk
from tkinter import *


class Game:


    def singleplayer(self):
        print("1")
        return 1

    def multiplayer(self):
        print("2")
        return 2

    def exit(self):
        sys.exit()

    # creating buttons
    def but(self, r):
        but1 = ttk.Button(r, text="Single Player")
        but1.pack(pady=10, ipadx=4, ipady=3)
        but1.config(command=lambda: self.singleplayer())

        but2 = ttk.Button(r, text="Multiplayer")
        but2.pack(pady=0, ipadx=4, ipady=3)
        but2.config(command=lambda: self.multiplayer())

        but3 = ttk.Button(r, text="Exit")
        but3.pack(pady=10, ipadx=4, ipady=3)
        but3.config(command=lambda: self.exit())


def main():
    root1 = Tk()
    root1.title("Tic Tac Toe")
    root1.geometry("400x200+150+200")

    style = ttk.Style()
    style.theme_use('clam')
    style.configure("TButton", font=20)

    game = Game()
    game.but(root1)

    root1.mainloop()


if __name__ == '__main__': main()
