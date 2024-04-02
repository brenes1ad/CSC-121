"""
mainGame.py -- main application for a simple tree-based 20-quesitons
sort of game. Tree will be self-updating polymorphic binary tree.

Tony Brenes
CSC121 W24
4/2/2024
"""

from queryNode import QueryNode
from guessNode import GuessNode

def main():
    """run the program: load tree, play rounds, save updated tree"""




    # load data from default.pkl file if exists, else create base case
    gameTree = QueryNode("Is your character the protagonist of Unity", GuessNode("Arno Dorian"),
                         GuessNode("Francois-Thomas Germian"))


    # greet user, ask if wants to play a game: ready?


    #enter game loop
    keepPlaying = True
    while keepPlaying:
        gameTree = gameTree.play()
        continueGame = input("Would you like to continue playing?" + "\n")
        if continueGame[0].lower() == "n":
            keepPlaying = False




    #ask if want to save? if yes, pickle current tree to new default file
    print("My work here is finished.")



if __name__ == "__main__":
    main()
