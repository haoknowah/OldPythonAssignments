import pickle
def supremeCourt():
    '''
supremeCourt=finds the justices in each state
@param infile=JusticeDict.dat file
@param dictOfJustice=dictionary containing data from infile
@param restart=keeps loop going if input was invalid
@param states=dictionary containing necissary keys and definitions
@param just=sorts through justices
@param stateList=list holding states in abc order
prints number of justices in each state
    '''
    try:
        infile=open("JusticesDict.dat", 'rb')
        dictOfJustice=pickle.load(infile)
        infile.close()
        states={}
        for just in dictOfJustice:
            if dictOfJustice[just]["state"] in states:
                states[dictOfJustice[just]["state"]]=states[dictOfJustice[just]["state"]]+1
            else:
                states[dictOfJustice[just]["state"]]=1
        stateList=list(states)
        stateList.sort()
        for state in range(len(stateList)):
            print(stateList[state], " has had ", states[stateList[state]], " justices.", sep="")
    except:
        print("Error in supremeCourt.")
if __name__ == "__main__":
    def test_supremeCourt():
        '''
test_supremeCourt()=tests the supremeCourt() method
@param cont=boolean that determines if program repeats
        '''
        try:
            cont=True
            while cont==True:
                supremeCourt()
                end=input("Continue? y or n ")
                if end.lower()=="n":
                    cont=False
        except:
            print("Error.")
    test_supremeCourt()
