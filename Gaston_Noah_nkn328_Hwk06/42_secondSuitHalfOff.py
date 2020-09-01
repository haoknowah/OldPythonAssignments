def secondSuitHalfOff():
    '''
determines sale price of two suits with one half off
@param one=suit one
@param two=suit two
    '''
    try:
        one=float(input("Enter the cost of suit one: "))
        two=float(input("Enter the cost of suit two: "))
        if one <= two:
            print("The total is: $",0.5*one+two, sep="")
        else:
            print("The total is: $",0.5*two+one, sep="")
    except:
        print("The men's clothing store only has dresses left.")

if __name__ == "__main__":
    print(__name__)
    try:
        def main():
            while(True):
                secondSuitHalfOff()
        main()
    except:
        print("The lights are on but no one is home.")
