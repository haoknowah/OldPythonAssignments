def supremeCourt():
    '''
supremeCourt=reads a list of justices and then finds the current justices
@param infile=file of justices being read
@param listOfJustice=list containing all the lines of the file
@param i=variable used to count number of lines when using split function
@param presidentJustices=sorted list of what lines from the file contain the
information needed
@param pres=variable used to cycle through the names of the presidents in the
list listOfJustice
prints the names of the current justices in order of when they joined
    '''
    try:
        infile=open("Justices.txt", 'r')
        listOfJustice=[line.rstrip() for line in infile]
        infile.close()
        for i in range(len(listOfJustice)):
            listOfJustice[i]=listOfJustice[i].split(",")
            listOfJustice[i][4] = eval(listOfJustice[i][4])
            listOfJustice[i][5] = eval(listOfJustice[i][5])
        presidentJustices=[]
        for pres in range(len(listOfJustice)):
            if listOfJustice[pres][5] == 0:
                presidentJustices.append(listOfJustice[pres])
        print("The current justices are: ")
        presidentJustices.sort(key=lambda join: join[4])
        for just in range(len(presidentJustices)):
            print(presidentJustices[just][0] + " " + presidentJustices[just][1])
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
