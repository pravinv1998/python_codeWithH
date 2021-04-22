'''
  accept no from user and compair it from existing one

'''

age = 22

def guess_game():
    for i in range(9):
        num = int(input("Enter the Age: "))
        if num == age and num < 100:
            print("You are Win!!!!! \nGame Over!")
            print(f"You guess no in {i + 1} guesses")
            break
        elif num > age and num < 100:
            print("Get smaller numbers...")
            print(f"{8 - i} guesses are left")
        elif num < age and num < 100:
            print("Get Bigger one")
            print(f"{8 - i} guesses are left")
        else:
            print("Over age,try smaller one...")
    else:
        print("Game Over!\nYou Loose,Try next time.")
        print(f" age is {age}")



guess_game()

guess_again = input("You want to guess again,\n if yes then type y or type n : ")
if guess_again == "y":
    guess_game()
elif guess_again == "n":
    print("Good By")




