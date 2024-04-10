"""
queryNode.py -- subclass of game tree that creates the query Node and subsequent gameplay for a guess

Tony Brenes
CSC121 W24
4/2/2024
"""

from gameTree import GameTree
import PySimpleGUI as sg

class QueryNode(GameTree):

    def play(self):
        while True:
            ans = sg.popup_yes_no(self.question, title="My Question")
            if ans is not None:
                break
        if ans == 'Yes':
            self.yesNode = self.yesNode.play()
        else:
            self.noNode = self.noNode.play()

        return self
