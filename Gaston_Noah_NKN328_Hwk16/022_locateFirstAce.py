try:
    import random
except ImportError as exc1:
    print(exc1)
def locateFirstAce():
    '''
locateFirstAce()=finds the first ace in a deck of cards and the average number
of draws it takes to reach the first ace after 100,000 tries
@param deck=list containing all of the cards in the deck
@param average=the average number of draws taken
@param shuffle=number of times shuffled
@param aces=the location of the aces in the deck
prints the average number of draws it would take to find an ace
    '''
    try:
        deck=[n for n in range(1,53)]
        average=0
        shuffle=0
        while shuffle <= 100000:
            aces=random.sample(deck, 4)
            average=average+min(aces)
            shuffle+=1
        average=average/100000
        print("The average number af cards drawn to reach an ace was ", average)
    except:
        print("The deck was nothing but jokers.")
if __name__ == "__main__":
    def test_locateFirstAce():
        '''
test_locateFirstAce()=tests the locateFirstAce() method
        '''
        try:
            locateFirstAce()
        except:
            print("There's a problem.")
    test_locateFirstAce()
