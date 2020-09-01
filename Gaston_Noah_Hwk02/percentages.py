def percentages():
    '''
converts a percent to decimal form
@param x=percentage to be converted
    '''
    try:
        x=float(input("Enter the percantage that you want as a decimal: "))
        print("Moving dicimal to the left twice....")
        print("The decimal form is: ",x/100)
    except:
        print("Try moving the decimal to the left two places.")
