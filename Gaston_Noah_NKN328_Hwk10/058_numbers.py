def numbers():
    '''
numbers()=sorts list of numbers using sumOfNumbers
@param numbers=list of numbers
    '''
    try:
        numbers = [865, 1169, 1208, 1243, 329]
        numbers=sumOfNumbers(numbers)
        print("Sorted by sum of digits: ")
        print(numbers)            
    except:
        print("Error, function.")
def sumOfNumbers(numbers):
    '''
sumOfNumbers()=finds the sum of the digits of all numbers in list by converting
each one to strings that can be seperated and stored in lists inside a list,
sorted by the sum of their parts and then have the lists recombined back into
a list of strings to be reassembled in order for return
@param newList=main list to hold the lists of the digits
@param newerList=list that holds digits for a number
@param finaList=list being returned (and yes, I purposely only put one L)
returns finaList
    '''
    try:
        newList = []
        for num in numbers:
            newerList = []
            num=str(num)
            for digit in num:
                digit=int(digit)
                newerList.append(digit)
            newList.append(newerList)
        newList.sort(key=sum)
        finaList = []
        for subList in newList:
            fNum=""
            for digit in subList:
                digit = str(digit)
                fNum = fNum + digit
            finaList.append(fNum)
        return finaList
    except:
        print("Error, subfunction.")
if __name__ == "__main__":
    '''
main method that tests the numbers function
    '''
    print(__name__)
    try:
        cont=True
        while cont==True:
            numbers()
            end=input("Continue? y or n ")
            if end.lower()=="n":
                cont=False
    except:
        print("Error.")
