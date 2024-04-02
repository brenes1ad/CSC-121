from gameTree import GameTree
from queryNode import QueryNode

class GuessNode(GameTree):

    def play(self):
        ans = input("Is it " + self.question + "?")
        #UPDATE SO IT KEEPS LOOPING UNTIL VALID RESPONSE
        if ans[0].lower() == 'y':
            print("Hah! Well, you can only expect so much from humans.")
            return self
        else:
            print("hmm... I give up...")
            # Ask for correct answer, save to correct yesval
            yesval = input("Enter your character as the correct answer")
            # Give me a question that's yes for yesval and no for self.question.
            #        Save to goodQuestion var
            goodQuestion = input("Enter a question that's yes to your character")

            # Return new QueryNode with goodQuestion, new GuessNode with yesval
            #        and self as old value
            return QueryNode(goodQuestion, GuessNode(yesval), self)