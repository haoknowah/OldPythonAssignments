try:
    from itertools import permutations
except ImportError as exc:
    print(exc)
def permutation(word):
    '''
permutation()=finds permutations of an input word
returns a list of the permutations
    '''
    try:
        return ["".join(char) for char in permutations(word)]            
    except:
        print("Unhandled exception.")
if __name__ == "__main__":
    def test_permutation():
        '''
test_permutation()=tests the permutation() method
@param cont=boolean that determines if program repeats
@param word=input word
@param good=boolean that shows if word is a valid input
prints permutations of input word
flair=makes sure that there are no repeat letters in word
        '''
        try:
            cont=True
            while cont==True:
                while True:
                    word=str(input("Enter a word with no repeated letters: "))
                    good=True
                    if word.isalpha()==False:
                        good=False
                    else:
                        for char in word:
                            if word.count(char) > 1:
                                good=False
                                break
                    if good==True:
                        break
                    else:
                        print("Not a proper word or repeats letters.")
                print(permutation(word))
                end=input("Reset? y or n ")
                if end.lower()=="n":
                    cont=False
        except:
            print("Something unexpected happenned.")
    test_permutation()
