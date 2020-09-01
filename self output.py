import os
def outputter(output):
    '''

    '''
    try:

    except:
        print("Error in outputter")
def isOutput():
    '''

    '''
    try:

    except:
        print("Error in isOutput.")
if __name__ == "__main__":
    def test_outputter():
        '''
test_primeFactors()=tests the primeFactors() method
@param cont=boolean that determines if program repeats
        '''
        try:
            cont=True
            while cont==True:
                name=input("Enter a name: ")
                fileOfNames(name.title())
                end=input("Continue? y or n ")
                if end.lower()=="n":
                    cont=False
        except:
            print("Error.")
    test_outputter()
