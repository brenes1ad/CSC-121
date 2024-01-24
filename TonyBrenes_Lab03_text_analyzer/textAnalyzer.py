"""
Main.py -- read in a text file from the current working directory as specified
by the runtime user using the runtime command line

T. Brenes
CSC121 W24
1/23/24
Lab3
"""

import os

class InvalidTitle(Exception):
    pass


def bookSearcher():
    # Do the following until a good book is found and input
    # Print directory listing
    # Query the user for a book file to input
    # Open the book file and read into a text string

    dirList = os.listdir()
    print("Pick one of these:")
    for fileName in dirList:
        if fileName.endswith(".txt"):
            print(fileName)
    # USE AN INPUT TO GET THE USER'S CHOICE
    # Use while loop and Try/Except for user input error
    while True:
        try:
            bookChoice = input("Enter a book choice from the previous list as written from list: ")
            if bookChoice not in dirList:
                raise InvalidTitle
            break
        except InvalidTitle:
            print("Book not listed, please try enter another text file ")

    f = open(bookChoice, "r")
    with open(bookChoice, "r", encoding="utf8") as f:
        bookText = f.read()

# Input words to search for and print out
# how many times it was found
# continue until no new  word is found
# compute how long it took to enter word from user
# and find word


    while True:
        count = 0
        searchWord = input("Enter word to search for in chosen book. Enter \"\" (empty string) to quit search. ")
        if searchWord == "":
            break
        for words in bookText.split():
            if searchWord.lower() == words.lower():
                count += 1
        print(f"{searchWord} was found {count} times \n")

bookSearcher()

