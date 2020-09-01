def wordReplacement():
    '''
replaces one word in the sentence for another
@param n=index of where the word is
    '''
    try:
        x=input("Enter a sentence: ")
        word=input("Type a word that occurs once in that sentence to find: ")
        drow=input("Type a word to replace it with: ")
        n=x.find(word)
        print(x[:n],drow,x[n+len(word):], sep="")
    except:
        l=input("Enter the number of times that you want to be laughed at as a whole number: ")
        print("ha"*l)
