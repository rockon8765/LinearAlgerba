from random import randint
123

def play():
    random_int=randint(0,100)

    while True:
        user_guess=int(input("What number did we guess (0-100)?"))

        if user_guess == random_int:
            print(f"You found the number ({random_int}). Congrats!")
            break

        if user_guess < random_int:
            print("Your number is less than the number we guess.")
            continue

        if user_guess > random_int:
           print("Your number is more than the number we guess.")
           continue


if __name__=='__main__':
    play()
