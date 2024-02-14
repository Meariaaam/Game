def main():

    import random

    print("Hello! Welcome to a game of Pig!")
    print("           9")
    print("     ,--.-'-,--.")
    print("     \\  /-~-\\  /")
    print("    / )' a a `( \\")
    print("   ( (  ,---.  ) )")
    print("    \\ `(_o_o_)' /")
    print("     \\   `-'   /")
    print("      | |---| |  ")
    print("      [_]   [_]")
    print("")
    print("Throw the dice!")

    dice = random.randint(1, 6)
    print(f"You got a {dice}!")

    if dice == 1:
        print("_____________")
        print("|           |")
        print("|           |")
        print("|     O     |")
        print("|           |")
        print("|___________|")
        
    elif dice == 2:
        print("_____________")
        print("|           |")
        print("|        O  |")
        print("|           |")
        print("|  O        |")
        print("|___________|")

    elif dice == 3:
        print("_____________")
        print("|           |")
        print("|        O  |")
        print("|     O     |")
        print("|  O        |")
        print("|___________|")

    elif dice == 4:
        print("_____________")
        print("|           |")
        print("|  O     O  |")
        print("|           |")
        print("|  O     O  |")
        print("|___________|")

    elif dice == 5:
        print("_____________")
        print("|           |")
        print("|  O     O  |")
        print("|     O     |")
        print("|  O     O  |")
        print("|___________|")

    elif dice == 6:
        print("_____________")
        print("|           |")
        print("|  O    O   |")
        print("|  O    O   |")
        print("|  O    O   |")
        print("|___________|")


if __name__ == "__main__":
    main()
