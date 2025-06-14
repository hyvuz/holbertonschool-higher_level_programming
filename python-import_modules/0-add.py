#!/usr/bin/python3
from add_0 import add  # Import the add function from the module (add_0)

a = 1                  # Define a in a line
b = 2                  # Define b in another line

if __name__ == "__main__":
    print("{} + {} = {}".format(a, b, add(a, b)))
