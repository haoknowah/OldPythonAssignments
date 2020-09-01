try:
    import random
except ImportError as exc:
    print(exc)
global moves
moves=["rock","paper","scissors"]
class Contestant:
    def __init__(self, player="com", score=0):
        self.score=score
        self.player=player
    def increaseScore(self):
        self.score+=1
    def getPlayer(self):
        return self.player
    def getPlay(self):
        return self.play()
    def __str__(self):
        return self.player + "  " + str(self.score)
class Human(Contestant):
    def setPlay(self, action):
        self.action=action
    def play(self):
        return self.action
class Computer(Contestant):
    def play(self):
        return random.sample(moves, 1)[0]


        
