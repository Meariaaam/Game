import random


def main():

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

    dice = random.randint(1, 6)
    print(dice)

    if __name__ == "__main__":
        main()
