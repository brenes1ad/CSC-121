from gameTree import GameTree
from queryNode import QueryNode
import PySimpleGUI as sg

class GuessNode(GameTree):

    def play(self):
        ans = sg.popup_yes_no("Is it " +self.question + "?", title="My Guess")
        #UPDATE SO IT KEEPS LOOPING UNTIL VALID RESPONSE
        if ans == 'Yes':
            sg.popup("Hah! Well, you can only expect so much from humans.")
            return self
        else:

            # Ask for correct answer, save to correct yesval
            yesval = sg.popup_get_text("Hmm.. I give up. Enter You character as the correct answer", title="Enter Answer")
            # Give me a question that's yes for yesval and no for self.question.
            #        Save to goodQuestion var
            goodQuestion = sg.popup_get_text("Enter a question that's yes to your character", title="Enter Question")

            # Return new QueryNode with goodQuestion, new GuessNode with yesval
            #        and self as old value
            return QueryNode(goodQuestion, GuessNode(yesval), self)