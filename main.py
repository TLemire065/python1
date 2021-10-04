# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from random import randint, randrange


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


def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.

    # Prints Top
    print("+-------" * 3, "+", sep="")
    for row in range(3):
        print("|       " * 3, "|", sep="")

        for column in range(3):
            # Prints Numbers/Values
            print("|  ", (board[row][column]), "  ", end="")
        print("|")
        # Prints Column Sides
        print("|       " * 3, "|", sep="")
        # Prints Row Bottoms
        print("+-------" * 3, "+", sep="")


def enter_move(board):
    # The function accepts the board's current status, asks the user about their move,
    # checks the input, and updates the board according to the user's decision.

    invalid = True

    try:
        while invalid:
            player_move = int(input("Enter your move: "))

            if player_move < 1 or player_move > 9:
                print("Invalid Position, Try Again")
                continue

            board_row = (player_move - 1) // 3
            board_column = (player_move - 1) % 3

            if board[board_row][board_column] in ["X", "O"]:
                print("That Space Is Already Played, Try Again")
                continue
            else:
                board[board_row][board_column] = "O"
                invalid = False
    except ValueError:
        print("Invalid Position, Try Again")
        enter_move(board)


def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares;
    # the list consists of tuples, while each tuple is a pair of row and column numbers.

    # Creates new list
    free_spaces = []

    for row in range(3):  # Gets each row
        for column in range(3):  # Gets each column
            if board[row][column] not in ["X", "O"]: free_spaces.append(
                (row, column))  # Check to see if X or O is in the board space, if not appends numbers to list

    return free_spaces  # Returns free spaces


def victory_for(board, sign):
    # The function analyzes the board's status in order to check if
    # the player using 'O's or 'X's has won the game

    # Sets Variables
    cross1 = cross2 = True

    for rc in range(3):

        # Checks Rows
        if board[rc][0] == sign and board[rc][1] == sign and board[rc][2] == sign: return True
        # Checks Columns
        if board[0][rc] == sign and board[1][rc] == sign and board[2][rc] == sign: return True
        # Checks 1 and 9 Diagonal
        if board[rc][rc] != sign: cross1 = False
        # Cheks 3 and 7 Diagonal
        if board[rc][2 - rc] != sign and board[2 - rc][rc]: cross2 = False

    if cross1 is True or cross2 is True:
        return True

    # No Winners
    return False


def draw_move(board):
    # The function draws the computer's move and updates the board.

    free_list = make_list_of_free_fields(board)

    random_space = randrange(len(free_list))

    row = (free_list[random_space])[0]
    column = (free_list[random_space])[1]

    board[row][column] = 'X'


def tictactoe():
    board = [[3 * j + i + 1 for i in range(3)] for j in range(3)]  # Creates board
    board[1][1] = "X"  # Sets X in the middle

    free_list = make_list_of_free_fields(board)

    while len(free_list):

        display_board(board)

        # Player's Turn
        enter_move(board)
        if victory_for(board, "O"):
            display_board(board)
            print("You Won")
            break

        # Computers Turn
        draw_move(board)
        if victory_for(board, "X"):
            display_board(board)
            print("You Lost")
            break

        # Checks If Game Is Tied
        free_list = make_list_of_free_fields(board)
        if len(free_list) == 0:
            display_board(board)
            print("Tied Game!")
            break


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    print("Week 1: Name Print\nWeek 2: Creating A Function\nWeek 3: Printing Arrays & Playing Coinflip\n"
          "Week 4: Tic-Tac-Toe\n")

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
    elif assignment_number == 4:
        tictactoe()
    else: print("Invalid Selection")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
