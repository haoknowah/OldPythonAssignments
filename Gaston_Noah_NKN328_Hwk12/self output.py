import os
def outputter(output):
    '''

    '''
    try:
        if isOutput() = True:
            create=open("OUTPUT.txt", 'w')
            create.close()
        infile=open("OUTPUT.txt", 'a')
        outList=[line.rstrip() for line in infile]
        for sep in range(len(outList)):
            outList[sep]=outList[sep] + "\n"
        infile.writelines(output)
        infile.close()
    except:
        print("Error in outputter")
def isOutput():
    '''

    '''
    try:
        return os.path.isfile("OUTPUT.txt")
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
                
                end=input("Continue? y or n ")
                if end.lower()=="n":
                    cont=False
        except:
            print("Error.")
    test_outputter()
