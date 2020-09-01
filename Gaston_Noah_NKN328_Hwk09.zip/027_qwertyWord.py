def qwertyWord(word):
    '''
not functioning
method qwertyWord determines if letters in word are all only in top row of keyboard
reurns whether or no they are(only showing not)
    '''
    try:
        word=word.lower()
        let=0
        qwerty=True
        while let <= len(word):
            if word[let:let] != "q" or word[let] != "w" or word[let] != "e" or word[let] != "r" or word[let] != "t" or word[let] != "y" or word[let] != "u" or word[let] != "i" or word[let] != "o" or word[let] != "p":
                qwerty=False
            let += 1
        return qwerty
    except:
        print("ErrOR.")
if __name__ == "__main__":
    '''
@param cont=determines whether or not to restart
@param word=input word
@param qwerty=whether ot not word is a qwerty word(only shows not)
    '''
    print(__name__)
    try:
        cont=True
        while cont==True:
            word=input("Type a word here: ")
            qwerty=qwertyWord(word)
            if qwerty == True:
                print(word, " is a qwerty word.", sep="")
            else:
                print(word, " isn't a qwerty word.", sep="")
            end=input("Do you wish to continue? y or n")
            if end.lower() == "n":
                cont=False
    except:
        print("Deleting browser history.")
