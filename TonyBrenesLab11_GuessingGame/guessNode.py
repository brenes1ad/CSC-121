"""
guessNode.py -- subclass of game tree that creates the guess Node and subsequent gameplay for a guess

Tony Brenes
CSC121 W24
4/2/2024
"""

from gameTree import GameTree
from queryNode import QueryNode
import PySimpleGUI as sg

class GuessNode(GameTree):

    def play(self):
        while True:
            ans = sg.popup_yes_no("Is it " +self.question + "?", title="My Guess")
            if ans is not None:
                break
        #UPDATE SO IT KEEPS LOOPING UNTIL VALID RESPONSE
        if ans == 'Yes':
            sg.popup("Hah! Well, you can only expect so much from humans.", title="LOSER!!")
            return self
        else:

            # Ask for correct answer, save to correct yesval
            while True:
                yesval = sg.popup_get_text("Hmm.. I give up. Enter You character as the correct answer", title="Enter Answer")
                if yesval is not None:
                    break
            # Give me a question that's yes for yesval and no for self.question.
            #        Save to goodQuestion var
            while True:
                goodQuestion = sg.popup_get_text("Enter a question that's yes to your character", title="Enter Question")
                if goodQuestion is not None:
                    break

            # Return new QueryNode with goodQuestion, new GuessNode with yesval
            #        and self as old value
            return QueryNode(goodQuestion, GuessNode(yesval), self)