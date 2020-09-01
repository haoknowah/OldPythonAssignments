def numbers():
    '''
numbers()=sorts a list of numbers by descending sum of their odd digits
    '''
    try:
        numbers = [865, 1169, 1208, 1243, 329]
        numbers.sort(key=sumOfNumbers, reverse=True)
        print(numbers)
        
    except:
        print("This is the last of the numbers for tonight.")
def sumOfNumbers(num):
    '''
the same thing as in 058 except the newerList part is replaced with loop to find
and store odd digits, which are then added together and returned to be sorted back
in the numbers() function
    '''
    try:
        newList = []
        num=str(num)
        for digit in num:
            digit=int(digit)
            if digit%2!=0:
                newList.append(digit)
        for subList in newList:
            fNum=0
            subList=str(subList)
            for digit in subList:
                digit = int(digit)
                fNum = fNum + digit
            fNum
        return fNum
    except:
        print("I think I need to keep this as a template function.")
if __name__ == "__main__":
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
