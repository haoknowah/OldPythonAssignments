import pickle
def supremeCourt():
    '''
supremeCourt=finds the information about input justice
@param person=input justice
@param infile=JusticeDict.dat file
@param dictOfJustice=dictionary containing data from infile
@param restart=keeps loop going if input was invalid
@param justices=dictionary containing necissary keys and definitions
@param just=sorts through justices
prints information about input justice 
    '''
    try:
        person=input("Type the name of a justice: ")
        infile=open("JusticesDict.dat", 'rb')
        dictOfJustice=pickle.load(infile)
        infile.close()
        restart=True
        justices={}
        while restart==True:
            for just in dictOfJustice:
                if just==person:
                    justices[just]=dictOfJustice[just]
                    restart=False
            if restart==True:
                person=input("Not a justice, try again: ")
        print("State: ", justices[person]["state"], sep=" ")
        print("Apointed in: ", justices[person]["yrAppt"], sep="")
        print("Appointed by: ", justices[person]["pres"], sep="")
        if justices[person]["yrLeft"]==0:
            print("Still in office.")
        else:
            print("Left in: ", justices[person]["yrLeft"], sep="")
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
