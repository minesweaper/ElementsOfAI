import random


def main():
    if random.random() <= 0.8:
        favourite = "dogs"
    elif random.random() <= 0.9:
        favourite = "cats"
    else:
        favourite = "bats"  # change this

    return print("I love " + favourite)


main()