def greatestCommonDivisor(numbers, div):
    '''
greatestCommonDivisor()=finds greatest common divisor of two input integers
using recursion
@param numbers=list of input numbers
@param div=divisor being tested
returns div when it has become greatest common divisor
    '''
    try:
        if numbers[0]%div==0 and numbers[1]%div==0:
            return div
        else:
            div-=1
            return greatestCommonDivisor(numbers, div)
    except:
        print("Unhandled exception.")
if __name__ == "__main__":
    def test_greatestCommonDivisor():
        '''
test_greatestCommonDivisor()=tests the greatestCommonDivisor() method
@param cont=boolean that determines if program repeats
@param numbers=list containing input numbers
@param first=first input number
@param second=second input number
prints greatest common divisor of two input numbers
flair=sorts out non integers and negatives
        '''
        try:
            cont=True
            while cont==True:
                try:
                    numbers=[]
                    first=int(input("Type a positive integer here:"))
                    while first<=0:
                        first=int(input("Try again: "))
                    numbers.append(first)
                    second=int(input("Type another positive integer:"))
                    while second<=0:
                        second=int(input("Try again: "))
                    numbers.append(second)
                    print(greatestCommonDivisor(numbers, div=min(numbers)))
                    end=input("Reset? y or n ")
                    if end.lower()=="n":
                        cont=False
                except ValueError as exc:
                    print(exc)
                    end=input("Reset? y or n ")
                    if end.lower()=="n":
                        cont=False
        except:
            print("Something unexpected happenned.")
    test_greatestCommonDivisor()
