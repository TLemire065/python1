# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


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
    #Calculates how many letters are in the words and prints it
    print(word, "has", len(word), "characters")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('Tyler')
    a2_function()




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
