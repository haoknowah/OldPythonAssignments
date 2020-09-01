def numbers():
    '''
numbers()=checks a file with numbers and finds the sum of the numbers in it
@param infile=read file containing the numbers
@param numList=list holding numbers from the file
@param numberSum=sum of numbers in the file
prints the sum of the numbers in the file
    '''
    try:
        infile=open("Numbers.txt", 'r')
        numList=[line.rstrip() for line in infile]
        numberSum=0
        for number in numList:
            number=int(number)
            numberSum=numberSum + number
        print(numberSum, " is the sum of the numbers in the file.", sep="")
        infile.close()
    except:
        print("Error in numbers.")
if __name__ == "__main__":
    def test_numbers():
        '''
test_numbers()=tests the numbers() method
@param cont=boolean that determines if program repeats
        '''
        try:
            cont=True
            while cont==True:
                numbers()
                end=input("Continue? y or n ")
                if end.lower()=="n":
                    cont=False
        except:
            print("Error.")
    test_numbers()
