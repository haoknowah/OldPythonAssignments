try:
    import contestant
except ImportError as exc:
    print(exc)
global moves
moves=["rock","paper","scissors"]
def rockPaperScissors():
    '''
plays game of rock paper scissors
@param player=player name
@param me, com=objects of contestant class
@param action=move performed
prints moves used, winner and current score
    '''
    try:
        player=input("Enter player name: ")
        me=contestant.Human(player)
        com=contestant.Computer()
        while True:
            action=input("Are you going to use rock, paper, or scissors? ")
            while action.lower() not in moves:
                action=input("Invalid, try again. ")
            me.setPlay(action)
            ranPlay=com.getPlay()
            print("CPU plays ", ranPlay)
            if (ranPlay=="rock" and me.getPlay()=="scissors") or \
            (ranPlay=="scissors" and me.getPlay()=="paper") or \
            (ranPlay=="paper" and me.getPlay()=="rock"):
                print("CPU wins.")
                com.increaseScore()
            elif ranPlay==me.getPlay():
                print("Draw")
            else:
                print("You win.")
                me.increaseScore()
            print(me, "\t", com)
            cont=input("Continue? y or n ")
            if cont.lower()=="n":
                break
            
    except:
        print("Unhandled exception.")
if __name__=="__main__":
    def test_rockPaperScissors():
        rockPaperScissors()
    test_rockPaperScissors()
