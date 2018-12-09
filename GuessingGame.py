import random


class GuessingGame:

    def __init__(self):
        self.ran_choice = random.randint(0, 10)

    def reset(self):
        print("\nResetting the number")
        self.ran_choice = random.randint(0, 10)

    def guess(self):

        while True:
            flag = True
            user_choice = int(input("Enter a number between 0-10: "))

            if user_choice == self.ran_choice:
                print("\n**correct choice**")
                break
            else:
                if user_choice < self.ran_choice:
                    print("\nWrong, guess higher")
                else:
                    print("\nWrong, guess lower")
                while flag:
                    choice = input("\nWould you like to guess again (y/n): ")
                    choice.lower()
                    if choice == 'n':
                        exit(0)
                    elif choice != 'y' and choice != 'n':
                        print("Enter correct choice")
                        continue
                    else:
                        flag = False


g = GuessingGame()
g.guess()
