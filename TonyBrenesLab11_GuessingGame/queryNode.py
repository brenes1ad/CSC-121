from gameTree import GameTree
import PySimpleGUI as sg

class QueryNode(GameTree):

    def play(self):
        ans = sg.popup_yes_no(self.question, title="My Question")
        if ans == 'Yes':
            self.yesNode = self.yesNode.play()
        else:
            self.noNode = self.noNode.play()

        return self
