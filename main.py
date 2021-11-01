import sys

if __name__ == "__main__":
    print("Arguments count: ", len(sys.argv))

    for i, args in enumerate(sys.argv):
        print(f"Argument{i:6}: {args}")