try:
    import random
    import pickle
except ImportError as exc1:
    print(exc1)
def bridge():
    '''
bridge()=draws a hand of 13 cards and finds the point total of the hand
@param infile=holds card data from DeckOfCardsList.dat
@param deck=holds the cards extracted from DeckOfCardsList.dat in infile
@param hand=holds 13 random cards taken from the deck
@param hpc=total number of points in hand
@param points=dictionary containing how many points the cards are worth
@param card=card from hand having its point value checked
prints the cards in hand and the total number of points from those cards
    '''
    try:
        infile=open("DeckOfCardsList.dat", 'rb')
        deck=pickle.load(infile)
    except FileNotFoundError as exc2:
        print(exc2)
    infile.close()
    try:
        hand=random.sample(deck, 13)
    except NameError as exc3:
        print(exc3)
    except TypeError as exc4:
        print(exc4)
    try:
        hpc=0
        points={"A":4, "K":3, "Q":2, "J":1}
        for card in hand:
            if card[0] in "AKQJ":
                hpc+=points[card[0]]
        print(hand)
        print("The total points are ", hpc)
    except KeyError as exc5:
        print(exc5)
    except TypeError as exc6:
        print(exc6)
    except:
        print("Unhandled exception")
if __name__ == "__main__":
    def test_bridge():
        '''
test_bridge()=tests the bridge() method
@param cont=boolean that determines if program repeats
        '''
        try:
            cont=True
            while cont==True:
                bridge()
                end=input("Continue? y or n ")
                if end.lower()=="n":
                    cont=False
        except:
            print("There was a problem.")
    test_bridge()
