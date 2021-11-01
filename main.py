# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import re

# Gets input from user
def user_input():
    user_string = input("Enter A String: ")
    return user_string


def string_split1(user_sentence):

    # Uses split method and then prints each word
    for word in user_sentence.split():
        print(word)



def string_split2(user_sentence):

    # Uses re split method and then prints each work
    string_split = re.split(r"\s+", user_sentence)
    for word in string_split:
        print(word)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # Gets users input
    user_sentence = user_input()
    # Invokes first string function
    string_split2(user_sentence)
    # Invokes second string function
    string_split2(user_sentence)
