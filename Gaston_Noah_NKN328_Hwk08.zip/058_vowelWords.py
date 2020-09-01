def vowelWords():
    '''
vowelWords()=determines if word has all vowels
checks each individual value as boolean
print whether or not word has all vowels
    '''
    try:
        word=input("Type a word here: ")
        a=False
        e=False
        i=False
        o=False
        u=False
        for ch in word.lower():
            if ch == "a":
                a=True
            elif ch == "e":
                e=True
            elif ch == "i":
                i=True
            elif ch == "o":
                o=True
            elif ch == "u":
                u=True
        if a==True and e==True and i==True and o==True and u==True:
            print("The word contains every vowel.")
        else:
            print("Missing vowels.")
    except:
        print("Error occured.")
if __name__=="__main__":
    print(__name__)
    vowelWords()
