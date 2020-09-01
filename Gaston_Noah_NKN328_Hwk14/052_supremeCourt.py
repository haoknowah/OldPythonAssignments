import pickle
def supremeCourt():
    '''
supremeCourt=finds the justices instated from an input state and year appointed
@param state=input state
@param infile=JusticeDict.dat file
@param dictOfJustice=dictionary containing data from infile
@param restart=keeps loop going if input was invalid
@param justices=dictionary containing necissary keys and definitions
@param just=sorts through justices
prints justices and when they joined 
    '''
    try:
        state=input("Type the abreviation of a state in all caps: ")
        infile=open("JusticesDict.dat", 'rb')
        dictOfJustice=pickle.load(infile)
        infile.close()
        restart=True
        justices={}
        while restart==True:
            for just in dictOfJustice:
                if dictOfJustice[just]["state"]==state:
                    justices[just]=dictOfJustice[just]
                    restart=False
            if restart==True:
                state=input("Not a state, try again, and don't give a staate of matter either: ")
        for just in justices:
            print(just, " was instated in ", justices[just]["yrAppt"], sep="")
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
