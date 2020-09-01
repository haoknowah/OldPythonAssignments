def analyzeASentence():
    '''
purpose is to determine the first and last words of a sentence
@param x=sentence
@param f=first word
@param l=last word
had to make it x[l+1:] in order to get rid of the extra space before the last word
    '''
    try:
        x=input("Type a sentence here: ")
        f=x.find(" ")
        l=x.rfind(" ")
        print("The first word of the sentence is ", x[0:f], " and the \
last word is ", x[l+1:], sep="")
    except:
        print("Error.")
if __name__ == "__main__":
    print(__name__)
    analyzeASentence()
