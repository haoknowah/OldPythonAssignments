def supremeCourt():
    '''
supremeCourt=reads a list of justices and then finds the ones instated by the
input president
@param president=input president that is being checked for justices instated
@param infile=file of justices being read
@param listOfJustice=list containing all the lines of the file
@param i=variable used to count number of lines when using split function
@param presidentJustices=sorted list of what lines from the file contain the
information needed
@param pres=variable used to cycle through the names of the presidents in the
list listOfJustice
prints the names of the justices appointed by input president by order of time
served
    '''
    try:
        president=input("Enter the name of a president: ")
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
            if listOfJustice[pres][2] == president:
                presidentJustices.append(listOfJustice[pres])
        presidentJustices.sort(key=lambda time: time[5]-time[4], reverse=True)
        print("The justices appointed by this president are: ")
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
