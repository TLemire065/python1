# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import re
import os


def os_module():
    # Saves as variable
    os_uname = str(os.uname())

    # Prints os version
    print('OS Version:', re.findall('(?<=version=)[^:]*',os_uname)[0])
    # Prints os machine
    print('OS Machine:', re.findall('(?<=machine=)[^/)]*', os_uname)[0])
    # Prints os name
    print('OS Name:', os.name)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    try:
        os_module()
    except AttributeError:
        print("Unable to execute, non-linux machine detected.")
