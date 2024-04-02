from gameTree import GameTree

class QueryNode(GameTree):

    def play(self):
        ans = input(self.question + " ('y' or 'n')")
        if ans[0].lower() == 'y':
            self.yesNode = self.yesNode.play()
        else:
            self.noNode = self.noNode.play()

        return self
