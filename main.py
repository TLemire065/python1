# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from random import randint


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# A function that prompts the user for a name, number, and word
def a2_function():
    # Asks for a name
    name = input("Enter your name: ")
    # Prints the inputted name
    print("Hello,", name)

    # Asks for a number
    number = float(input("Enter a number: "))
    # Multiples the inputted number by itself and prints it
    print(number, "x", number, "=", number * number)

    # Asks for a word
    word = input("Enter a word: ")
    # Calculates how many letters are in the words and prints it
    print(word, "has", len(word), "characters")


def a3_array():
    array = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

    # Gets array column index
    for i in range(len(array[0])):
        # Gets array row index
        for j in range(len(array)):
            # Prints array value based on row and column
            print(array[j][i], end='')
        print()


def a3_coinflip():
    # Gets user value
    user_value = int(input("Enter 1 or 0: "))
    # Generates a random number of 0 or 1
    random_value = randint(0, 1)

    # Compares users value to generated value
    if user_value == random_value: print("You Win!")
    else: print("You Lose!")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    print("Week 1: Name Print\nWeek 2: Creating A Function\nWeek 3: Printing Arrays & Playing Coinflip\n")

    assignment_number = int(input("Enter Week Number: "))

    if assignment_number == 1: print_hi('Tyler')
    elif assignment_number == 2: a2_function()
    elif assignment_number == 3:
        assignment_selection = int(input("Enter 0 for array function or 1 for coinflip function: "))
        if assignment_selection == 0:
            a3_array()
        elif assignment_selection == 1:
            a3_coinflip()
        else: print("Invalid Selection")
    else: print("Invalid Selection")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
