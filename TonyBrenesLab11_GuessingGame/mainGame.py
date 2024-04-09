"""
mainGame.py -- main application for a simple tree-based 20-quesitons
sort of game. Tree will be self-updating polymorphic binary tree.

Tony Brenes
CSC121 W24
4/2/2024
"""

from queryNode import QueryNode
from guessNode import GuessNode
import PySimpleGUI as sg
import pickle



def main():
    """run the program: load tree, play rounds, save updated tree"""

    # greet user, ask if wants to play a game: ready?
    sg.popup("Hey, lets play a fun game!", title="Guess the Assassin's Creed Character Game")


    # load data from .gametree.pkl file if exists, else create base case

    try:
        with open("treeout.pkl", "rb") as f:
            gameTree = pickle.load(f)
    except FileNotFoundError:
        gameTree = QueryNode("Is your character the protagonist of Unity", GuessNode("Arno Dorian"),
                             GuessNode("Francois-Thomas Germian"))


    #enter game loop
    keepPlaying = True
    while keepPlaying:
        gameTree = gameTree.play()
        if sg.popup_yes_no("Would you like to continue playing?", title="Continue?") != "Yes":
            keepPlaying = False





    #ask if want to save? if yes, pickle current tree to new default file
    wantToSave = sg.popup_yes_no("Do you want to save this tree of questions and answers?", title="save")
    if wantToSave == "Yes":
        with open("treeout.pkl", "wb") as f:
            pickle.dump(gameTree, f)

    sg.popup("My work here is finished.")



if __name__ == "__main__":
    main()
