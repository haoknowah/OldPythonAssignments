def numbers():
    '''
numbers()=sorts numbers by prime factor
@param numbers=list of numbers
    '''
    try:
        numbers = [865, 1169, 1208, 1243, 329]
        print("Sorted by last digit: ")
        numbers.sort(key=lastDigit, reverse=True)
        print(numbers)
    except:
        print("Error.")
def lastDigit(num):
    '''
lastDigit=checks last digit by turning number into string to check last character
    '''
    try:
        num=str(num)
        return num[-1]
    except:
        print("Error, subfunction.")

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
