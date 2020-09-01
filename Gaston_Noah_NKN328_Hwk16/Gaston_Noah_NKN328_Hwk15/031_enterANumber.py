def enterANumber():
    '''
enterANumber()=takes input number and tells what it is or if it is more than
100 or less than 1
@param number=input number
prints the input number
    '''
    try:
        number=int(input("Enter an integer numbered 1 through 100: "))
    except ValueError:
        print("Not an integer.")
    try:
        if number>=1 and number<=100:
            print("Your number is ", number)
        elif number<1:
            print("Number is too small.")
        elif number>100:
            print("Number is too large.")
    except:
        print("Error in enterANumber")
if __name__ == "__main__":
    def test_enterANumber():
        '''
test_enterANumber()=tests the enterANumber() method
@param cont=boolean that determines if program repeats
        '''
        try:
            cont=True
            while cont==True:
                enterANumber()
                end=input("Continue? y or n ")
                if end.lower()=="n":
                    cont=False
        except:
            print("Error, test.")
    test_enterANumber()
