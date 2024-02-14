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
    print(f"The dice shows the number: {dice}")


if __name__ == "__main__":
    main()
