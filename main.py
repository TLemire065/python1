# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def user_input():
    # Prompts user for string and returns it
    user_string = input("Enter any string: ")
    return user_string


def pig_translate(string):
    # Splits string into list
    words = string.split()
    # List of all vowels
    vowels = ['a', 'e', 'i', 'o', 'u']

    # Gets each word from list
    for i, word in enumerate(words):
        # Checks if starting letter is a vowel
        if word[0] in vowels:
            words[i] = words[i]+'yay'
        else:
            # Enumerates each letter in the word
            for j, letter in enumerate(word):
                # Checks if letter is a vowel, if so it add all previous letters to the end and appends ay
                if letter in vowels:
                    words[i] = word[j:] + word[:j] + 'ay'
                    break
                # If word has no vowel, reverses word and appends ay
                elif j+1 == len(word):
                    words[i] = word[-1:] + word[:-1] + 'ay'

    # Combines list of words
    pig_latin = ' '.join(words)
    # Returns translated pig latin
    return pig_latin


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    user_input = user_input()
    print("Translated string:", pig_translate(user_input))