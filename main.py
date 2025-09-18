import random

def guess_the_number():
    print("Welcome to guess the number 🎲")
    print("I think about a number between 1 and 100.")

    secretnumber = random.randint(1,100)
    trys = 0

    while True:
        tipp = input("Your tip: ")

        if not tipp.isdigit():
            print("Please choose a number!")
            continue

        tipp = int(tipp)
        
        if tipp < secretnumber:
            print("To low!")
            trys += 1
        elif tipp > secretnumber:
            print("To high!")
            trys += 1
        else:
            print(f"Congratulations!🎉 You are right, the number was {secretnumber}.")
            print(f"You needed {trys} trys.")
            break

guess_the_number()

