try:
    import pCard
except ImportError as exc:
    print(exc)
def cards():
    '''
cards()=displays a face card
@param deck=holds object of class PlayingCard
returns deck object now containing a face card
    '''
    try:
        deck=pCard.PlayingCard()
        while True:
            deck.selectAtRandom()
            if deck.getRank()=="jack" or deck.getRank()=="queen" or deck.getRank()=="king":
                break
        return deck
    except:
        print("Unhandled exception.")
if __name__=="__main__":
    def test_cards():
        '''
tests the cards() method
@param cont=determines if loop restarts
        '''
        try:
            cont=True
            while cont==True:
                card=cards()
                print("The card is a ", card.getRank(), " of ", card.getSuit(),".", sep="")
                end=input("Do you wish to continue? y or n ")
                if end.lower()=="n":
                    cont=False
        except:
            print("Unhandled exception.")
    test_cards()
    '''
import random
class PlayingCard:
    def __init__(self, rank="queen", suit="hearts"):
        self._rank = rank
        self._suit = suit
    def setRank(self, rank):
        self._rank = rank
    def setSuit(self, suit):
        self._suit = suit
    def getRank(self):
        return self._rank
    def getSuit(self):
        return self._suit
    def selectAtRandom(self):
     ## Randomly select a rank and a suit.
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9',
        "10", "jack", "queen", "king", "ace"]
        self._rank = random.choice(ranks)
        self._suit = random.choice(["spades", "hearts", "clubs", "diamonds"])
    def __str__(self):
        return(self._rank + " of " + self._suit)
    '''
