try:
    import random
except ImportError as exc:
    print(exc)
def guessMyNumber():
    '''
guessMyNumber()=picks a random number 1 through 100 and has user attempt
to guess it
@param numberOfTries=number of guesses made
@param n=random number
@param guess=gusses number
prints whether or not guessed number was too high, too low, or correct
    '''
    try:
        numberOfTries = 1
        n = random.randint(1, 100)
        print("I've thought of a number from 1 through 100.")
        while True:
            try:
                guess = int(input("Guess the number: "))
                break
            except ValueError:
                numberOfTries += 1
                print("You did not enter a number, but this still counts as a try.")
        while guess != n:
            numberOfTries += 1
            if (guess > 100) or (guess < 1):
                print("Number must be from 1 through 100, you wasted a guess.")
            elif guess > n:
                print("Too high")
            elif guess < n:
                print("Too low")
            while True:
                try:
                   guess = int(input("Try again: "))
                   break
                except ValueError:
                   numberOfTries += 1
                   print("You did not enter a number, wasted a guess.")

        print("Correct.", end=" ")
        if numberOfTries == 1:
            print("You got it in one guess.")
        else:
            print("You took", numberOfTries, "guesses.")
    except:
        print("Unhandled exception.")
if __name__ == "__main__":
    def test_guessMyNumber():
        '''
test_guessMyNumber()=tests the guessMyNumber() method
@param cont=boolean that determines if program repeats
        '''
        try:
            cont=True
            while cont==True:
                guessMyNumber()
                end=input("Reset? y or n ")
                if end.lower()=="n":
                    cont=False
        except:
            print("Something unexpected happenned.")
    test_guessMyNumber()

