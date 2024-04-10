"""
mainGame.py -- main application for a simple tree-based 20-quesitons
sort of game. Tree will be self-updating polymorphic binary tree.

Tony Brenes
CSC121 W24
4/2/2024

All code was used to assist in the creation of David Amo's code as well
"""

from queryNode import QueryNode
from guessNode import GuessNode
import PySimpleGUI as sg
import pickle



def main():
    """run the program: load tree, play rounds, save updated tree"""
    """
    for every pop-up except the first introduction and continue, pressing x-button will bring back the same prompt to avoid empty 
    tree Nodes, for intro pop-up, x-button will quit out of the game, pressing x-button on continue popup serves as pressing No
    """

    # greet user, ask if wants to play a game: ready?
    start = sg.popup("Hey, lets play a fun game!", title="Guess the Assassin's Creed Character Game")
    if start is None:
        return


    # load data from .gametree.pkl file if exists, else create base case

    try:
        with open("treeout.pkl", "rb") as f:
            gameTree = pickle.load(f)
    except FileNotFoundError:
        gameTree = QueryNode("Is your character the protagonist of Unity", GuessNode("Arno Dorian"),
                             GuessNode("Francois-Thomas Germian"))


    #enter game loop
    while True:
        gameTree = gameTree.play()
        if sg.popup_yes_no("Would you like to continue playing?", title="Continue?") != "Yes":
            break





    #ask if want to save? if yes, pickle current tree to new default file
    while True:
        wantToSave = sg.popup_yes_no("Do you want to save this tree of questions and answers?", title="Save?")
        if wantToSave is not None:
            break
    if wantToSave == "Yes":
        with open("treeout.pkl", "wb") as f:
            pickle.dump(gameTree, f)

    sg.popup("My work here is finished.")



if __name__ == "__main__":
    main()
