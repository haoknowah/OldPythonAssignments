def greatestCommonDivisor():
    '''
determines what the greatest common divisor is for 2 integers
@param x=first integer
@param y=second integer
@param lis=list containing integers to help sort them, meaning that this could be expanded by adding more variables in
@param i=minimum number of the integers that could be used as a starting point to count down from
    '''
    try:
        x=int(input("Enter an integer: "))
        y=int(input("Enter another integer: "))
        lis=[x,y]
        i=min(lis)
        if x%i != 0 or y%i != 0:
            while x%i!=0 or y%i!=0:
                i-=1
            print("The greatest common divisor is ", i, sep="")
        else:
            print("Greatest common divisor is",i)
    except:
        print("To infinity and beyond.")
if __name__ == "__main__":
    print(__name__)
    try:
        def main():
            while(True):
                greatestCommonDivisor()
        main()
    except:
        print("The lights are on but no one is home.")

