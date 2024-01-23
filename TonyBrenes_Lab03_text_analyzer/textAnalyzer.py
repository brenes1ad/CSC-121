"""
Main.py -- read in a text file from the current working directory as specified
by the runtime user using the runtime command line

T. Brenes
CSC121 W24
1/23/24
Lab3
"""

import os

def bookSearcher():

    #Do the following until a good book is found and input
    #Print directory listing
    #Query the user for a book file to input
    #Open the book file and read into a text string

    while True:
        dirList = os.listdir()
        print("Hello")
        print("Pick one of these:")
        for fileName in dirList:
            if fileName.endswith(".txt"):
                print(fileName)
        #USE AN INPUT TO GET THE USER'S CHOICE
        #Use while loop and Try/Except for user input error
        bookChoice = "MobyDick.txt"

        f = open(bookChoice, "r")
        with open(bookChoice, "r") as f:
         booktext = f.read()

        print("%s has %d characters" %(bookChoice, len(booktext)))
        print(booktext[:100])

        #Input words to search for and print out
        #how many times it was found
        #continue until no new  word is found
        #compute how long it took to enter word from user
        #and find word

        break





if __name__ == "__main_":
    bookSearcher()