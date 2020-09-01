def maxFunction(numbers):
    '''
method maxFunction determines what the highest number in list is by sorting it, reversing
it, and then checking the first number so that it doesn't have to check how long
it is
returns max number in list
    '''
    try:
        numbers.sort()
        numbers.reverse()
        return numbers[0]
    except:
        print("Infinity.")
if __name__ == "__main__":
    '''
@param times=determines whether or not to repeat the loop
@param numbers=list of numbers to check for max created through loop that continues until stopped
prints max number in list
    '''
    print(__name__)
    try:
        numbers=[]
        times=""
        while times !="n":
            x=float(input("Enter a number: "))
            numbers.append(x)
            times=input("Type n to end.")
        print("The max is:", maxFunction(numbers))
    except:
        print("Error.")
        
