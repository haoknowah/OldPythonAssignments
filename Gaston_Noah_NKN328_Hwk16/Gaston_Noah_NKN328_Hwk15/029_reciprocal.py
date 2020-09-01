def reciprocal():
    '''
reciprocal()=finds the reciprocal of a nonzero integer
@param n=input integer
@param reciprocal=reciprocal of input integer
prints the reciprocal of input integer
    '''
    while True:
        try:
            n = int(input("Enter a nonzero integer: "))
        except ValueError:
            print("Not an integer or at least not in the form of one.")
        else:
            try:
                if n != 0:
                    reciprocal = 1 / n
                    print("The reciprocal of {0} is {1:,.3f}".format(n, reciprocal))
                    break
                else:
                    print("You entered zero. Try again.")
            except:
                print("Error in reciprocal.")
if __name__ == "__main__":
    def test_reciprocal():
        '''
test_reciprocal()=tests the reciprocal() method
@param cont=boolean that determines if program repeats
        '''
        try:
            cont=True
            while cont==True:
                reciprocal()
                end=input("Continue? y or n ")
                if end.lower()=="n":
                    cont=False
        except:
            print("Error, test.")
    test_reciprocal()
