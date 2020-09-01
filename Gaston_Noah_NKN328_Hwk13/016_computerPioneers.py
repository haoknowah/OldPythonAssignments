def computerPioneers():
    '''
computerPioneers=reads a file of people who have made important contributions to programming
and list's their names, then listing the accomplishments of whichever one is entered
@param infile=file with the list of computer pioneers and their accomplishments
@param pie=list of the computer pioneers and their accomplishments
@param counter=counts the number of times the names that have been used
@param pioneer=pioneer being searched for
@param exist=boolean used to break loop
@param person=person being checked in list
prints list of computer pioneers and the accomplishments of the one specified
    '''
    try:
        infile=open("Pioneers.txt", 'r')
        pie=[line.rstrip() for line in infile]
        infile.close()
        for line in range(len(pie)):
            pie[line]=pie[line].split(",")
        counter=0
        while counter+3 < len(pie):
            print("{0:<22s}{1:<20s}{2:<20s}{3:20s}".format(pie[counter][0],
                                                           pie[counter+1][0],
                                                           pie[counter+2][0],
                                                           pie[counter+3][0]))
            counter += 4
        while True:
            pioneer=input("Type the name of a pioneer: ")
            exist=False
            for person in range(len(pie)):
                if pioneer==pie[person][0]:
                    print(" ".join(pie[person]))
                    exist=True
            if exist==False:
                print("Not a pioneer.")
            else:
                break
    except:
        print("Error in computerPioneers.")
if __name__ == "__main__":
    def test_computerPioneers():
        '''
test_computerPioneers()=tests the computerPioneers() method
@param cont=boolean that determines if program repeats
        '''
        try:
            cont=True
            while cont==True:
                computerPioneers()
                end=input("Continue? y or n ")
                if end.lower()=="n":
                    cont=False
        except:
            print("Error.")
    test_computerPioneers()
