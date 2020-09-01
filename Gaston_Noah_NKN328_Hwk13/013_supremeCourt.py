def supremeCourt():
    '''
supremeCourt=reads a list of justices and then finds the ones in office during
1980
@param infile=file of justices being read
@param listOfJustice=list containing all the lines of the file
@param i=variable used to count number of lines when using split function
@param presidentJustices=sorted list of what lines from the file contain the
information needed
@param pres=variable used to cycle through the names of the presidents in the
list listOfJustice
@param just=variable used to sort through presidentJustices to format and print
them
prints the names of the justices in office during 1980
    '''
    try:
        infile=open("Justices.txt", 'r')
        listOfJustice=[line.rstrip() for line in infile]
        infile.close()
        for i in range(len(listOfJustice)):
            listOfJustice[i]=listOfJustice[i].split(",")
            listOfJustice[i][4] = eval(listOfJustice[i][4])
            listOfJustice[i][5] = eval(listOfJustice[i][5])
            if listOfJustice[i][5] == 0:
                listOfJustice[i][5]=2015
        presidentJustices=[]
        for pres in range(len(listOfJustice)):
            if listOfJustice[pres][4]<=1980 and listOfJustice[pres][5]>=1980:
                presidentJustices.append(listOfJustice[pres])
        presidentJustices.sort(key=lambda join: join[4])
        print("{0:<20s}{1:<20s}".format("Justice: ", "Assigned president: "))
        for just in range(len(presidentJustices)):
            justice=presidentJustices[just][0]+" "+presidentJustices[just][1]
            print("{0:<20s}{1:<20s}".format(justice, presidentJustices[just][2]))
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

