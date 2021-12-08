# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

class Bird:

    # Initial object creation and attributes
    def __init__(self, name):
        self.name = name
        self.color = ""
        self.species = "Bird"
        self.can_fly = True

    # Print method
    def speak(self):
        print("My name is {}".format(self.name))

    # Gets name attribute
    def get_name(self):
        return self.name

    # Sets name attribute
    def set_name(self, name):
        self.name = name

    # Set color attribute
    def set_color(self, color):
        self.color = color


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # Prompt user for name
    x = input("Enter A Name For Bird 1: ")
    Bird1 = Bird(x)

    # Prompt user for name
    x = input("Enter A Name For Bird 2: ")
    Bird2 = Bird(x)

    # Prompt user for color of bird1
    x = input(f"What color is {Bird1.get_name()}?: ")
    Bird1.set_color(x)

    # Prompt user for color of bird2
    x = input(f"What color is {Bird2.get_name()}?: ")
    Bird2.set_color(x)

    # Bird1 speak method
    Bird1.speak()
    # Bird2 speak method
    Bird2.speak()

    # Initiates list
    method_list = []

    # Loops through Bird class to find defined methods
    for i in dir(Bird):
        if not i.startswith("__"):
            method_list.append(i)

    # Prints defined methods
    print("Class Methods:", method_list)
    # Prints Bird1 attributes
    print(Bird1.name, "attributes:", Bird1.__dict__)
    # Prints Bird2 attributes
    print(Bird2.name, "attributes:", Bird2.__dict__)

