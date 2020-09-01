try:
    import random
except ImportError as exc1:
    print(exc1)
def rockPaperScissors():
    '''
rockPaperScissors()=plays a game of rock, paper, scissors between two players
@param janken=list with choices of what to use or what plays are availlable
@param player1=list containing input name and play of first player
@param player2=list containing input name and play of second player
prints name of each player and what they played
prints which player won based on play
flair notes: janken is the Japanese name for rock, paper, scissors and added
a function that allows players to input their name
    '''
    try:
        janken=["Rock", "Paper", "Scissors"]
        player1=[input("Enter name of player 1: "), random.choice(janken)]
        player2=[input("Enter name of player 2: "), random.choice(janken)]
        print(player1[0], " played ", player1[1], sep="")
        print(player2[0], " played ", player2[1], sep="")
    except NameError as exc2:
        print(exc2)
    except TypeError as exc3:
        print(exc3)
    except:
        print("Where are lizard and spock?")
    try:
        if player1[1]=="Rock" and player2[1]=="Scissors":
            print(player1[0]," wins.")
        elif player1[1]=="Scissors" and player2[1]=="Paper":
            print(player1[0]," wins.")
        elif player1[1]=="Paper" and player2[1]=="Rock":
            print(player1[0]," wins.")
        elif player1[1]==player2[1]:
            print("Tie.")
        else:
            print(player2[0]," wins.")
    except ValueError as exc4:
        print(exc4)
if __name__ == "__main__":
    def test_rockPaperScissors():
        '''
test_rockPaperScissors()=tests the rockPaperScissors() method
@param cont=boolean that determines if program repeats
        '''
        try:
            cont=True
            while cont==True:
                rockPaperScissors()
                end=input("Reset? y or n ")
                if end.lower()=="n":
                    cont=False
        except:
            print("Something unexpected happenned.")
    test_rockPaperScissors()
