def alphabeticalOrder(L):
    '''
alphabeticalOrder()=checks to see if input list of letters has letters
in abc order
@param L=input list
    '''
    try:
        abc=False
        if len(L)==1:
            abc=True
        elif L[0]<=L[1]:
            abc=alphabeticalOrder(L[1:])
        return abc
    except:
        print("Unhandled exception.")
if __name__=="__main__":
    def test_alphabeticalOrder():
        '''
tests if list is in abc order
@param L=test list in abc order
@param LNot=test list not in abc order
prints whether list is in abc order
        '''
        L=["a","b","c"]
        LNot=["a","c","b"]
        print("Is the list in abc order: ", alphabeticalOrder(L))
        print("Is the list in abc order: ", alphabeticalOrder(LNot))
    test_alphabeticalOrder()
