def alphabeticalOrder():
    '''
alphabeticalOrder()=determines if letters in word are in abc order
@param word=input word to check
print whether or not word was in abc order
    '''
    try:
        word=input("Enter a word: ")
        if word == "".join(sorted(word)):
            print("The word is in alphabetical order.")
        else:
            print("Word is not in alphabetical order.")
    except:
        print("Thor Ragnarok comes out on Febuary 20.")
if __name__ == "__main__":
    print(__name__)
    alphabeticalOrder()
