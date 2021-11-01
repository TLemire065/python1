import sys


def string_manipulation1(args):
    # Combines listed args
    args = ' '.join(args)
    # Checks if there are only lowercase letters
    if args.islower():
        print("The string only consists of lowercase letters")
    # Checks if there are only uppercase letters
    elif args.isupper():
        print("The string only consists of uppercase letters")
    else:
        print("The string consists of lower and uppercase letters")


def string_manipulation2(args):
    # Combines listed args
    args = ' '.join(args)
    # Capitalizes string
    capitalized_string = args.upper()
    print("String capitalized:", capitalized_string)
    # Titles string
    titled_string = args.title()
    print("String titled:", titled_string)


if __name__ == "__main__":

    string_manipulation1(sys.argv)
    string_manipulation2(sys.argv)
