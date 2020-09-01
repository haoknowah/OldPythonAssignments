def sumOfNumbers(numbers, i=0):
    '''
sumOfNumbers()=finds sum of list of numbers
@param numbers=list of input numbers
@param i=sum of numbers
returns i which is sum of numbers in list numbers
    '''
    try:
        if len(numbers)<1:
            return i
        else:
            return sumOfNumbers(numbers[1:], i+numbers[0])
    except:
        print("Unhandled exception.")
if __name__ == "__main__":
    def test_sumOfNumbers():
        '''
test_sumOfNumbers()=tests the sumOfNumbers() method
@param cont=boolean that determines if program repeats
@param numbers=list of input numbers
@param addition=input number
prints sum of numbers in list numbers
        '''
        try:
            cont=True
            while cont==True:
                numbers=[]
                while True:
                    addition=input("Type a number or end to stop adding: ")
                    if addition=="end":
                        break
                    elif addition.isdigit()!=True:
                        print("Not a number.")
                    else:
                        numbers.append(float(addition))
                print(sumOfNumbers(numbers))
                end=input("Reset? y or n ")
                if end.lower()=="n":
                    cont=False
        except:
            print("Something unexpected happenned.")
    test_sumOfNumbers()
