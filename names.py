# docs.python.org/3/library/functions.html#open
# 7:15:38 Harvard CS50’s Introduction to Programming with Python – Full University Course

name = input("What's your name? ")

# Open and automatically close a file
with open("names.txt", "a") as file:
    file.write(f"{name}\n")
