import os
def fileOfNames():
    '''
fileOfNames()=reads a file containing a list of names and then adds an input
name to that list before putting that list in a new file, deleting the original
list and changing the name of the new list to that of the deleted one
@param infile=input file with prime, unmodified original list
@param outfile=copy of the list that is modified to with method so it can
be cleaned and started again from scratch if so desired
@param nameList=list containing all of the names from the file that gets added to
@param final=variable holding the file that is to replace Names2.txt
note that the made file is called yub.txt as a reference to the ewoks from
Star Wars, yub was also a favorite paramater or place holder name when coding
java in previous classes
@param name=input name to add
outputs a new file replacing Names2.txt
made seperate Names2.txt file so that the original would still be there and
could be used as repeatable reference
    '''
    try:
        infile=open("Names.txt", 'r')
        outfile=open("Names2.txt", 'r')
        outfile.close()
        nameList=[line.rstrip() for line in infile]
        infile.close()
        final=open("yub.txt", 'w')
        while True:
            name=input("Enter a name: ")
            name=name.title()
            if nameList.count(name) == 0 and name.isalpha()==True:
                nameList.append(name)
            else:
                print("That name already exists.")
            cont=input("Type n to quit: ")
            if cont == "n":
                break
        nameList.sort()
        for sep in range(len(nameList)):
            nameList[sep]=nameList[sep] + "\n"
        final.writelines(nameList)
        final.close()
        os.remove("Names2.txt")
        os.rename("yub.txt", "Names2.txt")
    except:
        print("Error in fileOfNames")
if __name__ == "__main__":
    def test_fileOfNames():
        '''
test_fileOfNames()=tests the fileOfNames() method
@param cont=boolean that determines if program repeats
        '''
        try:
            cont=True
            while cont==True:
                fileOfNames()
                end=input("Continue? y or n ")
                if end.lower()=="n":
                    cont=False
        except:
            print("Error.")
    test_fileOfNames()
