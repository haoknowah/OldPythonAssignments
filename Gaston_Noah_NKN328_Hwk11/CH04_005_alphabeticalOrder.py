def isTripleConsecutive(word):
    '''
isTripleConsecutive(word)=determines if three of the letters in the word are in abc order
@param n=length of word
@param word=word being checked from input
@param i=characters in the string word
@param threeLetters=slice of three consecutive letters in word
return=true or false value depending on whether or not there are three letters in abc order
    '''
    try:
        n=len(word)
        for i in range(n-2):
            threeLetters=word[i:i+3]
            if (ord(threeLetters[0:1]) + 1== ord(threeLetters[1:2]) and
                ord(threeLetters[1:2]) + 1== ord(threeLetters[2:3])):
                return True
        return False
    except:
        print("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
if __name__ == "__main__":
    def test_isTripleConsecutive():
        '''
test_isTripleConsecutive()=tests the isTripleConsecutive function
@param cont=determines if program repeats itself
@param consec=boolean holding returned value from isTripleConsecutive(word)
prints the word and whether or not it had three letters in abc order
        '''
        try:
            cont=True
            while cont==True:
                word=input("Enter a word here: ")
                word=word.lower()
                if word.isalpha()==True:
                    consec=isTripleConsecutive(word)
                    if consec==True:
                        print(word, "has three letters in abc order.")
                    else:
                        print(word, "does not have three letters in abc order.")
                    end=input("Continue? y or n ")
                    if end.lower()=="n":
                        cont=False
                else:
                    print("That is not a word.")
        except:
            print("Error.")
    test_isTripleConsecutive()
