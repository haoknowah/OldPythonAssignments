import pickle
def letterFrequency():
    '''
letterFrequency=finds number of times each letter was used
@param sentence=input sentence
@param freq=dictionary containing the number of timeseach letter was used
@param wordList=list containing each letter used
prints the number of times each letter was used from greatest to least
    '''
    try:
        sentence=input("Enter a sentence: ")
        sentence=sentence.lower()
        freq=createFrequencyDictionary(sentence)
        wordList=[]
        for word in freq.keys():
            if word.isalpha()==True:
                wordList.append((word, freq[word]))
        wordList.sort(key=lambda x: x[1], reverse=True)
        for word in wordList:
            print(word[0], ": ", word[1], sep="")
    except:
        print("Error in letterFrequency.")
def createFrequencyDictionary(listOfWords):
    '''
taken from text
    '''
 ## Create dictionary with each item having the form word:word frequency.
    freq = {} # an empty dictionary
    for word in listOfWords:
        freq[word] = 0
    for word in listOfWords:
        freq[word] = freq[word] + 1
    return freq

if __name__ == "__main__":
    def test_letterFrequency():
        '''
test_letterFrequency()=tests the letterFrequency() method
@param cont=boolean that determines if program repeats
        '''
        try:
            cont=True
            while cont==True:
                letterFrequency()
                end=input("Continue? y or n ")
                if end.lower()=="n":
                    cont=False
        except:
            print("Error.")
    test_letterFrequency()
